from enum import Enum
from typing import List


class Caesar:
    _alphabet: List[str] = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                            "s", "t", "u", "v", "w", "x", "y", "z"]

    _alphabet_len = len(_alphabet)

    class Direction(Enum):
        LEFT = 1
        RIGHT = 2

    @classmethod
    def encrypt(cls, plain_txt: str, shift: int):
        return cls._routine(message=plain_txt, shift=shift, direction=cls.Direction.LEFT)

    @classmethod
    def decrypt(cls, cipher_txt: str, shift: int):
        return cls._routine(message=cipher_txt, shift=shift, direction=cls.Direction.RIGHT)

    @classmethod
    def _routine(cls, message: str, shift: int, direction: Direction):
        shifted_alphabet: List[str] = cls._shift_alphabet(shift=shift, direction=direction)
        plain_chars: List[str] = [char for char in message]

        cipher_chars: List[str] = []
        for char in plain_chars:
            index = cls._alphabet.index(char)
            cipher_chars.append(shifted_alphabet[index])

        return "".join(cipher_chars)

    @classmethod
    def _shift_alphabet(cls, shift: int, direction: Direction):
        if direction is cls.Direction.LEFT:
            appendix: List[str] = cls._alphabet[0: shift]
            suffix: List[str] = cls._alphabet[shift:len(cls._alphabet)]
        else:
            appendix: List[str] = cls._alphabet[0:(cls._alphabet_len - shift)]
            suffix: List[str] = cls._alphabet[cls._alphabet_len - shift: cls._alphabet_len]

        return suffix + appendix
