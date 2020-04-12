from random import randrange

import pytest

from cipher.caeser import Caesar
from cipher.test_helper import TestHelper

_cipher_params_c1 = [
    {
        "shift": 4,
        "cipher": "",
        "plain": ""
    },
    {
        "shift": 4,
        "plain": "helloworld",
        "cipher": "lippsasvph"
    },
    {
        "shift": 6,
        "plain": "helloworld",
        "cipher": "nkrrucuxrj"
    },
    {
        "shift": 26,
        "plain": "helloworld",
        "cipher": "helloworld"
    },
]


class TestCaesar:

    @pytest.mark.parametrize("params", [
        {
            "shift": 4,
            "should": (
                    "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
                    "q",
                    "r", "s", "t", "u", "v"),
            "direction": Caesar.Direction.RIGHT
        },
        {
            "shift": 6,
            "should": (
                    "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
                    "o",
                    "p", "q", "r", "s", "t"),
            "direction": Caesar.Direction.RIGHT
        },
        {
            "shift": 26,
            "should": (
                    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                    "u",
                    "v", "w", "x", "y", "z"),
            "direction": Caesar.Direction.RIGHT
        },
        {
            "shift": 52,
            "should": (
                    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                    "u",
                    "v", "w", "x", "y", "z"),
            "direction": Caesar.Direction.RIGHT
        },
        {
            "shift": 4,
            "should": (
                    "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                    "y",
                    "z", "a", "b", "c", "d"),
            "direction": Caesar.Direction.LEFT
        },
        {
            "shift": 6,
            "should": (
                    "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                    "a",
                    "b", "c", "d", "e", "f"),
            "direction": Caesar.Direction.LEFT
        },
        {
            "shift": 26,
            "should": (
                    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                    "u",
                    "v", "w", "x", "y", "z"),
            "direction": Caesar.Direction.LEFT
        },
        {
            "shift": 52,
            "should": (
                    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                    "u",
                    "v", "w", "x", "y", "z"),
            "direction": Caesar.Direction.LEFT
        },
    ])
    def test_shift_alphabet(self, params):
        assert Caesar._shift_alphabet(shift=params["shift"], direction=params["direction"]) == params["should"]

    @pytest.mark.parametrize("params", _cipher_params_c1)
    def test_decrypt(self, params):
        assert Caesar.decrypt(msg=params["cipher"], shift=params["shift"]) == params["plain"]

    @pytest.mark.parametrize("params", _cipher_params_c1)
    def test_encrypt(self, params):
        assert Caesar.encrypt(msg=params["plain"], shift=params["shift"]) == params["cipher"]

    @pytest.mark.parametrize("params", [{"shift": randrange(start=0, step=1, stop=100), "msg": msg} for msg in
                                        TestHelper.gen_x_words(100)])
    def test_cycle_random(self, params):
        assert params["msg"] == Caesar.decrypt(
            msg=Caesar.encrypt(
                msg=params["msg"],
                shift=params["shift"]
            ),
            shift=params["shift"]
        )
