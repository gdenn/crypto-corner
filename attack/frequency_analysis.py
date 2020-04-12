from typing import Dict


class FrequencyAnalysis:
    _letter_frequency_table_en = {
        "e": 12.02,
        "t": 9.10,
        "a": 8.12,
        "o": 7.68,
        "i": 7.31,
        "n": 6.95,
        "s": 6.28,
        "r": 6.02,
        "h": 5.92,
        "d": 4.32,
        "l": 3.98,
        "u": 2.88,
        "c": 2.71,
        "m": 2.61,
        "f": 2.30,
        "y": 2.11,
        "w": 2.09,
        "g": 2.03,
        "p": 1.82,
        "b": 1.49,
        "v": 1.11,
        "k": 0.69,
        "x": 0.17,
        "q": 0.11,
        "j": 0.10,
        "z": 0.07
    }

    @classmethod
    def _decrypt(cls, msg: str, lan="en"):
        frquency_chart: Dict[str, int] = cls._build_frequency_chart(msg=msg)

    @classmethod
    def _build_frequency_chart(cls, msg: str) -> Dict[str, int]:
        frequency_chart = {}
        for cipher_char in msg:
            if cipher_char not in frequency_chart:
                frequency_chart[cipher_char] = 1
            else:
                frequency_chart[cipher_char] = frequency_chart[cipher_char] + 1
        return frequency_chart
