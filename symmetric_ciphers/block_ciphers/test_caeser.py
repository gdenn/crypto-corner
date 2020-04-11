from random import seed, sample, randrange

import pytest

from symmetric_ciphers.block_ciphers.caeser import Caesar

# a b c d e f g h i j k l m n o p q r s t u v w x y z
# g h i j k l m n o p q r s t u v w x y z a b c d  e f

@pytest.mark.parametrize("params", [
    {
        "shift": 4,
        "should": ["w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
                   "q", "r", "s", "t", "u", "v"],
        "direction": Caesar.Direction.RIGHT
    },
    {
        "shift": 6,
        "should": ["u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
                   "o", "p", "q", "r", "s", "t"],
        "direction": Caesar.Direction.RIGHT
    },
    {
        "shift": 26,
        "should": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                   "s", "t", "u", "v", "w", "x", "y", "z"],
        "direction": Caesar.Direction.RIGHT
    },
    {
        "shift": 52,
        "should": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                   "s", "t", "u", "v", "w", "x", "y", "z"],
        "direction": Caesar.Direction.RIGHT
    },
    {
        "shift": 4,
        "should": ["e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
                   "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d"],
        "direction": Caesar.Direction.LEFT
    },
    {
        "shift": 6,
        "should": ["g", "h", "i", "j", "k", "l", "m", "n",
                   "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f"],
        "direction": Caesar.Direction.LEFT
    },
    {
        "shift": 26,
        "should": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                   "s", "t", "u", "v", "w", "x", "y", "z"],
        "direction": Caesar.Direction.LEFT
    },
    {
        "shift": 52,
        "should": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                   "s", "t", "u", "v", "w", "x", "y", "z"],
        "direction": Caesar.Direction.LEFT
    },
])
def test_shift_alphabet(params):
    assert Caesar._shift_alphabet(shift=params["shift"], direction=params["direction"]) == params["should"]


@pytest.mark.parametrize("params", [
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
])
def test_decrypt(params):
    assert Caesar.decrypt(cipher_txt=params["cipher"], shift=params["shift"]) == params["plain"]


@pytest.mark.parametrize("params", [
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
])
def test_encrypt(params):
    assert Caesar.encrypt(plain_txt=params["plain"], shift=params["shift"]) == params["cipher"]


def _gen_payload():
    seed(123)
    payload = Caesar._alphabet
    random_shift = randrange(start=0, stop=100000000, step=1)
    random_txt = "".join(sample(payload, len(payload)))
    return random_shift, random_txt


@pytest.mark.repeat(1000)
def test_cycle_random():
    shift, txt = _gen_payload()
    assert txt == Caesar.decrypt(
        cipher_txt=Caesar.encrypt(
            plain_txt=txt,
            shift=shift
        ),
        shift=shift
    )
