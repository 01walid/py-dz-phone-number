import pytest

from dz_phone_number import DZPhoneNumber


def test_immutability(valid_random_number):
    dz_phone_number = DZPhoneNumber(valid_random_number())
    d = dict()
    s = set()
    d[dz_phone_number] = 1
    s.add(dz_phone_number)
    assert dz_phone_number in s and dz_phone_number in d
