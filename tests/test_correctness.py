import pytest

from dz_phone_number import DZPhoneNumber, InvalidDZPhoneNumber


def test_invalid_phone_numbers(invalid_phone_numbers):
    for number in invalid_phone_numbers:
        with pytest.raises(InvalidDZPhoneNumber):
            DZPhoneNumber(number)


def test_valid_phone_numbers_with_some_formatting(valid_phone_numbers):
    for number in valid_phone_numbers:
        dz_phone_number = DZPhoneNumber(number)
        assert dz_phone_number.raw_number == number
