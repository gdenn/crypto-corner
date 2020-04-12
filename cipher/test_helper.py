from random import seed, sample
from typing import List


def gen_plain_msg(alphabet: List[str]) -> str:
    seed(123)
    random_txt = "".join(sample(alphabet, len(alphabet)))
    return random_txt
