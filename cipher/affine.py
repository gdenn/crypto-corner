from math import gcd
from typing import List, Callable

from exception.invalid_argument import InvalidArgumentException


class Affine:
    _algorithm = "affine cipher"

    _alphabet: List[str] = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                            "s", "t", "u", "v", "w", "x", "y", "z"]

    _alphabet_len = len(_alphabet)

    _inversion_table = {1: 1, 3: 9, 5: 21, 7: 15, 9: 3, 11: 19, 15: 7, 17: 23, 19: 11, 21: 5, 23: 17, 25: 25}

    @classmethod
    def encrypt(cls, msg: str, a: int, b: int) -> str:
        return cls._routine(char_function=cls._encrypt_char, msg=msg, a=a, b=b)

    @classmethod
    def decrypt(cls, msg: str, a: int, b: int) -> str:
        return cls._routine(char_function=cls._decrypt_char, msg=msg, a=a, b=b)

    @classmethod
    def _routine(cls, char_function: Callable[[str, int, int], str], msg: str, a: int, b: int):
        if gcd(Affine._alphabet_len, a) != 1:
            raise InvalidArgumentException(
                algorithm=cls._algorithm,
                argument="a",
                reason="expected gcd(a, k) == 1 for a: {a}".format(a=a)
            )

        if not (0 <= b < cls._alphabet_len):
            raise InvalidArgumentException(
                algorithm=cls._algorithm,
                argument="b",
                reason="expected 0 <= b < {alphabet_len} for b: {b}".format(alphabet_len=cls._alphabet_len, b=b)
            )

        char_list: List[str] = [c for c in msg]
        index_list: List[int] = [cls._alphabet.index(i) for i in char_list]
        converted_msg: List[str] = [char_function(x, a, b) for x in index_list]
        return "".join(converted_msg)

    @classmethod
    def _encrypt_char(cls, index: int, a: int, b: int) -> str:
        cipher_index = (a * index + b) % cls._alphabet_len
        return cls._alphabet[cipher_index]

    @classmethod
    def _decrypt_char(cls, index: int, a: int, b: int) -> str:
        inverse_a: int = cls._inversion_table[a]
        plain_index = (inverse_a * (index - b)) % cls._alphabet_len
        return cls._alphabet[plain_index]
