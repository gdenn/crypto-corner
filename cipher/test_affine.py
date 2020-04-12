from typing import List

import pytest

from cipher.affine import Affine
from cipher.test_helper import gen_plain_msg
from exception.invalid_argument import InvalidArgumentException


@pytest.fixture
def sound_a() -> List[str]:
    return [3, 5, 7, 9, 11, 15, 17, 19, 21, 23]


class TestAffine:
    @pytest.mark.parametrize("b", [0, 27, 28])
    def test_invalid_b(self, b):
        with pytest.raises(InvalidArgumentException):
            Affine.encrypt(msg="foo", a=1, b=b)

    @pytest.mark.parametrize("a", [2, 4, 6, 8, 10, 12, 13, 14, 16, 18, 20, 22, 24])
    def test_invalid_a(self, a):
        with pytest.raises(InvalidArgumentException):
            Affine.encrypt(msg="foo", a=a, b=25)

    @pytest.mark.repeat(100)
    def test_generated(self, sound_a: List[str]):
        """Generate some plain txt's and check if decrypt(encrypt(x,..) == plain"""
        plain_txt = gen_plain_msg(alphabet=Affine._alphabet)

        for a in sound_a:
            for b in range(0, 26):
                cipher_txt = Affine.encrypt(msg=plain_txt, a=a, b=b)
                assert plain_txt != cipher_txt

                lo_plain_txt = Affine.decrypt(msg=cipher_txt, a=a, b=b)
                assert plain_txt == lo_plain_txt
