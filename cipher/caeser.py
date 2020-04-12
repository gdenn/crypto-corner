from enum import Enum
from typing import List

from cipher.alphabet import Alphabet
from cipher.crypto_helper import CryptoHelper


class Caesar:

    class Direction(Enum):
        LEFT = 1
        RIGHT = 2

    @classmethod
    @CryptoHelper.read_from_file
    @CryptoHelper.ignore_whitespaces
    def encrypt(cls, msg: str, shift: int):
        return cls._routine(message=msg, shift=shift, direction=cls.Direction.LEFT)

    @classmethod
    @CryptoHelper.read_from_file
    @CryptoHelper.ignore_whitespaces
    def decrypt(cls, msg: str, shift: int):
        return cls._routine(message=msg, shift=shift, direction=cls.Direction.RIGHT)

    @classmethod
    def _routine(cls, message: str, shift: int, direction: Direction):
        shifted_alphabet: List[str] = cls._shift_alphabet(shift=shift, direction=direction)
        plain_chars: List[str] = [char for char in message]

        cipher_chars: List[str] = []
        for char in plain_chars:
            index = Alphabet.alphabet.index(char)
            cipher_chars.append(shifted_alphabet[index])

        return "".join(cipher_chars)

    @classmethod
    def _shift_alphabet(cls, shift: int, direction: Direction):
        shift = shift % Alphabet.alphabet_len
        if direction is cls.Direction.LEFT:
            appendix: List[str] = Alphabet.alphabet[0: shift]
            suffix: List[str] = Alphabet.alphabet[shift:Alphabet.alphabet_len]
        else:
            appendix: List[str] = Alphabet.alphabet[0:(Alphabet.alphabet_len - shift)]
            suffix: List[str] = Alphabet.alphabet[Alphabet.alphabet_len - shift: Alphabet.alphabet_len]

        return suffix + appendix
