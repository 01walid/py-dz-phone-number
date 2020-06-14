import pytest

from dz_phone_number import DZPhoneNumber


def test_is_value_error():
    with pytest.raises(ValueError):
        DZPhoneNumber("bla bla")
