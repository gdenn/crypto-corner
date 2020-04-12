from typing import List

import pytest

from cipher.affine import Affine
from cipher.test_helper import gen_plain_msg


@pytest.fixture
def sound_a() -> List[str]:
    return [3, 5, 7, 9, 11, 15, 17, 19, 21, 23]


class TestAffine:

    @pytest.mark.repeat(100)
    def test_generated(self, sound_a: List[str]):
        plain_txt = gen_plain_msg(alphabet=Affine._alphabet)

        for a in sound_a:
            for b in range(0, 26):
                cipher_txt = Affine.encrypt(msg=plain_txt, a=a, b=b)
                assert plain_txt != cipher_txt

                lo_plain_txt = Affine.decrypt(msg=cipher_txt, a=a, b=b)
                assert plain_txt == lo_plain_txt
