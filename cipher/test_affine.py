from typing import List

import pytest

from cipher.affine import Affine
from cipher.test_helper import TestHelper
from exception.invalid_argument import InvalidArgumentException


@pytest.fixture
def sound_a() -> List[str]:
    return [3, 5, 7, 9, 11, 15, 17, 19, 21, 23]


class TestAffine:
    @pytest.mark.parametrize("params", [
        {"index": 1, "a": 3, "b": 3, "expected": "g"},
        {"index": 1, "a": 5, "b": 12, "expected": "r"},
        {"index": 5, "a": 5, "b": 12, "expected": "l"},
        {"index": 25, "a": 5, "b": 12, "expected": "h"},
    ])
    def test_encrypt_char(self, params):
        assert Affine._encrypt_char(index=params["index"], a=params["a"], b=params["b"]) == params["expected"]

    @pytest.mark.parametrize("params", [
        {"index": 6, "a": 3, "b": 3, "expected": "b"},
        {"index": 17, "a": 5, "b": 12, "expected": "b"},
        {"index": 11, "a": 5, "b": 12, "expected": "f"},
        {"index": 7, "a": 5, "b": 12, "expected": "z"},
    ])
    def test_decrypt_char(self, params):
        assert Affine._decrypt_char(index=params["index"], a=params["a"], b=params["b"]) == params["expected"]

    @pytest.mark.parametrize("b", [-1, 27, 28])
    def test_invalid_b(self, b):
        with pytest.raises(InvalidArgumentException):
            Affine.encrypt(msg="foo", a=1, b=b)

    @pytest.mark.parametrize("a", [2, 4, 6, 8, 10, 12, 13, 14, 16, 18, 20, 22, 24])
    def test_invalid_a(self, a):
        with pytest.raises(InvalidArgumentException):
            Affine.encrypt(msg="foo", a=a, b=25)

    @pytest.mark.parametrize("msg", TestHelper.gen_x_words(50))
    def test_generated(self, msg: List[str], sound_a: List[str]):
        for a in sound_a:
            for b in range(0, 26):
                cipher_txt = Affine.encrypt(msg=msg, a=a, b=b)
                assert msg != cipher_txt

                lo_plain_txt = Affine.decrypt(msg=cipher_txt, a=a, b=b)
                assert msg == lo_plain_txt
