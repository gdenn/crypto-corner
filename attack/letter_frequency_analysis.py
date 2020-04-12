import copy

import numpy as np
import matplotlib.pyplot as plt

from typing import Dict

from cipher.crypto_helper import CryptoHelper


class LetterFrequencyAnalysis:
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
    @CryptoHelper.read_from_file
    @CryptoHelper.ignore_whitespaces
    def analyze(cls, msg: str, lan="en"):
        frequency_chart, total_count = cls._build_frequency_chart(msg=msg)
        cls._plot_frequency_bar_chart_total(frequency_bar_chart=frequency_chart, total=total_count)
        frequency_chart_percentage = cls._transform_to_percentage(frequency_chart=frequency_chart, total=total_count)
        cls._plot_frequency_bar_chart_percentage(frequency_bar_chart=frequency_chart_percentage)

    @classmethod
    def _build_frequency_chart(cls, msg: str) -> (Dict[str, int], int):
        frequency_chart = {}
        total_count = 0
        for cipher_char in msg:
            if cipher_char not in frequency_chart:
                frequency_chart[cipher_char] = 1
            else:
                frequency_chart[cipher_char] = frequency_chart[cipher_char] + 1
            total_count += 1

        return frequency_chart, total_count

    @classmethod
    def _transform_to_percentage(cls, frequency_chart: Dict[str, int], total: int):
        cc_frequency_chart = copy.deepcopy(frequency_chart)
        for letter in cc_frequency_chart:
            total_value = cc_frequency_chart[letter]
            percentage = (total_value / total) * 100
            cc_frequency_chart[letter] = percentage

        return cc_frequency_chart

    @classmethod
    def _plot_frequency_bar_chart_total(cls, frequency_bar_chart: Dict[str, int], total: int):
        objects = frequency_bar_chart.keys()
        y_pos = np.arange(len(objects))
        performance = frequency_bar_chart.values()

        plt.bar(y_pos, performance, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel("Occurrences (Total was {total})".format(total=total))
        plt.title("Letter Frequency in Cipher Text (Total)")

        plt.show()

    @classmethod
    def _plot_frequency_bar_chart_percentage(cls, frequency_bar_chart: Dict[str, int]):
        objects = frequency_bar_chart.keys()
        y_pos = np.arange(len(objects))
        performance = frequency_bar_chart.values()

        plt.bar(y_pos, performance, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel("Occurrences in Percentage %)")
        plt.title("Letter Frequency in Cipher Text (Percentage)")

        plt.show()

