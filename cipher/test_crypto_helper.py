from typing import List

import pytest

from cipher.crypto_helper import CryptoHelper
from cipher.test_helper import gen_plain_msg

alphabet: List[str] = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                       "s", "t", "u", "v", "w", "x", "y", "z", " "]


class TestCryptoHelper:
    @pytest.mark.parametrize("msg", [gen_plain_msg(alphabet) for _ in range(0, 50)])
    def test_handle_whitespaces(self, msg: str):
        stripped, whitespace_index_list = CryptoHelper._strip_whitespaces(msg=msg)
        assert " " not in stripped
        recovered = CryptoHelper._recover_whitespaces(msg=stripped, whitespace_index_list=whitespace_index_list)
        assert recovered == msg

    @pytest.mark.parametrize("msg", [gen_plain_msg(alphabet) for _ in range(0, 50)])
    def test_strip_whitespaces(self, msg: str):
        stripped, whitespace_index_list = CryptoHelper._strip_whitespaces(msg=msg)

        for index in whitespace_index_list:
            assert msg[index] == " "

        assert " " not in stripped

    @pytest.mark.parametrize("params", [
        {"msg": "helloworld", "whitespaces": [5], "expected": "hello world"},
        {"msg": "thefancydog", "whitespaces": [3, 9], "expected": "the fancy dog"},
    ])
    def test_recover_whitespaces(self, params):
        assert CryptoHelper._recover_whitespaces(
            msg=params["msg"],
            whitespace_index_list=params["whitespaces"]
        ) == params["expected"]
