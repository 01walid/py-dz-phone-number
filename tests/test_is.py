import pytest

from dz_phone_number import DZPhoneNumber, LandlinePrefix


def test_is_mobile():
    number = DZPhoneNumber("0512345678")
    assert number.is_mobile()
    assert not number.is_landline()


def test_is_landline():
    number = DZPhoneNumber("038123456")
    assert number.is_landline()
    assert not number.is_mobile()


def test_is_ooredoo():
    number = DZPhoneNumber("0512345678")
    assert number.is_ooredoo()
    assert not number.is_djezzy()
    assert not number.is_mobilis()


def test_is_djezzy():
    number = DZPhoneNumber("0712345678")
    assert number.is_djezzy()
    assert not number.is_ooredoo()
    assert not number.is_mobilis()


def test_is_mobilis():
    number = DZPhoneNumber("0612345678")
    assert number.is_mobilis()
    assert not number.is_ooredoo()
    assert not number.is_djezzy()


def test_is_wilayas():

    for wilaya, dial_number in LandlinePrefix.__members__.items():
        pn = DZPhoneNumber(f"0{dial_number.value}123456")
        attr = getattr(pn, f"is_{wilaya.lower()}")
        assert attr()
