import pytest

from dz_phone_number import DZPhoneNumber


def test_immutability(valid_random_number):
    dz_phone_number = DZPhoneNumber(valid_random_number())
    dz_phone_number2 = dz_phone_number.with_number(valid_random_number())

    assert dz_phone_number is not dz_phone_number2

    # Explicitly setting an attribute is prohibited
    with pytest.raises(TypeError):
        dz_phone_number.number = valid_random_number()
