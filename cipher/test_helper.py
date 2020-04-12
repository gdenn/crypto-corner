from random import seed, sample
from typing import List

from cipher.alphabet import Alphabet


class TestHelper:

    @classmethod
    def gen_word(cls, whitespaces=True) -> str:
        alphabet = Alphabet.alphabet
        alphabet_len = Alphabet.alphabet_len

        if whitespaces:
            alphabet += [" "]
            alphabet_len += 1

        random_txt = "".join(sample(alphabet, alphabet_len))

        return random_txt

    @classmethod
    def gen_x_words(cls, x: int, whitespaces=True):
        words: List[str] = []
        for _ in range(0, x):
            words.append(TestHelper.gen_word(whitespaces=whitespaces))

        return words
