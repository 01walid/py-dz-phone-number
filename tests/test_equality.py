import pytest

from dz_phone_number import DZPhoneNumber


def test_equality():
    dz_phone_number = DZPhoneNumber("0550123456")
    dz_phone_number2 = DZPhoneNumber("+213 550123456")
    assert dz_phone_number == dz_phone_number2

    dz_phone_number = DZPhoneNumber("0550123456")
    dz_phone_number2 = DZPhoneNumber("00213 550123456")
    assert dz_phone_number == dz_phone_number2

    dz_phone_number = DZPhoneNumber("+(213)550123456")
    dz_phone_number2 = DZPhoneNumber("0 55-012-34-56")
    assert dz_phone_number == dz_phone_number2


def test_inequality():
    dz_phone_number = DZPhoneNumber("0550123456")
    dz_phone_number2 = DZPhoneNumber("0650123456")
    assert dz_phone_number != dz_phone_number2
