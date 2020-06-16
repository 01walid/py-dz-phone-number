from __future__ import annotations

import re
from dataclasses import dataclass, field
from enum import Flag, IntFlag, unique
from typing import List, Union, Callable, Optional, Any

from .enums import CountryCode, LandlinePrefix, MobileOperator
from .exceptions import InvalidDZPhoneNumber


class DZPhoneNumber:
    """
    DZPhoneNumber represents a valid Algerian phone number as an object value.
    """

    # Define slots for immutability:
    # see: https://docs.python.org/3/reference/datamodel.html#slots
    # There's no TRUE immutability in Python, but this, along overriding __setattr__
    # and __delattr__ make it hard to alter the object once initialized.
    __slots__ = ["number", "indicative", "operator_or_region", "suffix", "raw_number"]

    def __init__(
        self,
        number: Optional[str] = None,
        indicative: Optional[str] = "0",
        operator_or_region: Optional[str] = None,
        suffix: Optional[str] = None,
    ):
        number = number or f"{indicative}{operator_or_region}{suffix}"
        self._set_number(number)

    def is_mobile(self) -> bool:
        return isinstance(self.operator_or_region, MobileOperator)

    def is_landline(self) -> bool:
        return isinstance(self.operator_or_region, LandlinePrefix)

    def replace(
        self,
        indicative: Union[str, None] = None,
        operator_or_region: Union[str, None] = None,
        suffix: Optional[str] = None,
    ) -> DZPhoneNumber:
        """
        Inspired from datetime.replace(month, day, hour, minute, second..)
        This replaces only a part of the phone number and returns a new instance.
        """
        indicative = indicative or self.indicative.value
        operator_or_region = operator_or_region or self.operator_or_region.value
        suffix = suffix or self.suffix
        # Makes a new instance
        return DZPhoneNumber(
            indicative=indicative, operator_or_region=operator_or_region, suffix=suffix
        )

    def get_pattern(self) -> re.Pattern:
        """
        Get all possible Landline and Mobile phone number prefixes and constructs
        a pre-compiled `Pattern` object ready for use.
        This uses Python regex grouping feature to isolate the country code, 
        Operator or region prefix, and the number itself.  
        """
        landline_re = "|".join([str(o) for o in LandlinePrefix.all()])
        mobile_re = "|".join([str(o) for o in MobileOperator.all()])

        # TODO: Explain this regex and why it's written like this (its conditional statement within)
        global_re = rf"\A(00213|\+213|0)({landline_re})?(?(2)([0-9]{{6}})|({mobile_re})([0-9]{{8}}))\Z"
        return re.compile(global_re)

    def _is_(self, operator_or_region: str) -> Callable:
        """
        Checks where `operator_or_region` matches the ones in this object instance.
        return: a callable rather than a bool or a value.
        """

        def is_match():
            return self.operator_or_region.is_of_equal_value(operator_or_region)

        return is_match  # return a callable for familiarity

    def with_number(self, number):
        return self.from_string(number)

    @classmethod
    def from_string(cls, number: str) -> DZPhoneNumber:
        """
        Acts like a named constructor. Accepts a number and returns a new instance
        of this class. 
        """
        return cls(number)

    def _set_number(self, number: str):
        object.__setattr__(self, "raw_number", number)
        if not isinstance(number, str):
            self.__raise_invalid()

        number = self._normalize_number(number)
        pattern = self.get_pattern()
        it_matches = pattern.match(number)

        if it_matches:
            indicative, operator_or_region, suffix = tuple(
                x for x in it_matches.groups() if x is not None
            )
            object.__setattr__(self, "indicative", CountryCode(indicative))
            object.__setattr__(
                self,
                "operator_or_region",
                self.get_operator_or_region_by_number(operator_or_region),
            )
            object.__setattr__(self, "suffix", suffix)
        else:
            self.__raise_invalid()

        object.__setattr__(self, "number", number)

    def get_operator_or_region_by_number(
        self, number: Union[str, int]
    ) -> Union[MobileOperator, LandlinePrefix]:
        number = int(number)
        return (
            MobileOperator(number)
            if number in MobileOperator.all()
            else LandlinePrefix(number)
        )

    def _normalize_number(self, value: str) -> str:
        """
        Removes some common chars from the number raw value.
        We want to support some valid-looking number given with some formatting.
        "valid-looking" and "formatting" are not well defined. There's no spec
        that dictates how to format Algerian phone numbers. This just use what's
        common. Which can be subjective. 
        This method can be refactored or removed at a later stage. 
        """
        # Remove trailing whitespace
        number = value.strip()

        # The number shouldn't start with a dash before we proceed to removing dashes
        if number.startswith("-") or number.endswith("-"):
            self.__raise_invalid()

        # Remove some formatting chars, but just up to their possible occurrences.
        chars_to_remove = {"-": 5, " ": 13, "(": 1, ")": 1, ".": 5}
        for char, count in chars_to_remove.items():
            number = number.replace(char, "", count)
        return number

    def __raise_invalid(self):
        """
        Just raise our custom alias of ValueError. It's nicer to tell the user
        which number is exactly not right. Thus `self.raw_number` was stored and
        reported here.
        """
        raise InvalidDZPhoneNumber(
            f"{self.raw_number} is invalid Algerian phone number"
        )

    # Overrides of some magic (a.k.a dunder) methods

    def __getattr__(self, name: str) -> Any:
        """
        This is some meta programming.
        We want a generic `is_SOMETHING` method defined on this object. Where
        `SOMETHING` could be: `djezzy`, `ooredoo`, `annaba`, `blida` ..etc
        without having to implement a dedicated method for each possible value
        of `SOMETHING`.
        """
        # we're only interested of attributes that start with `is_`
        if name.startswith("is_"):
            # get is what?
            operator_or_region_str = name.replace("is_", "").upper()
            # pass it to the `_is_` method to resolve.
            return self._is_(operator_or_region_str)

        raise AttributeError

    def __eq__(self, other: object) -> bool:
        """
        This is what's known as operator overload for other languages.
        overriding this method tells the interpretter how to compare two 
        python objects. In our case, it'll make it possible to do:
        number1 == number2, where `number1` and `number2` are both an instance of
        `DZPhoneNumber`.
        """
        if not isinstance(other, DZPhoneNumber):
            raise TypeError("Expected object of type DZPhoneNumber got", type(other))

        return (
            self.operator_or_region.value == other.operator_or_region.value
            and self.suffix == other.suffix
        )

    def __hash__(self):
        """
        For true equality, __hash__ needs to be defined.
        see: https://docs.python.org/3/reference/datamodel.html#object.__hash__
        a nice read: https://hynek.me/articles/hashes-and-equality/
        """
        return hash((self.indicative, self.operator_or_region, self.suffix))

    def __str__(self) -> str:
        """
        This define what's returned when you call `str(DZPhonenumberInstance)`.
        equivalent to both casting and to_string() in other languages.
        """
        return self.number

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}:{self.indicative.LOCAL} - {self.operator_or_region.describe()} - {self.suffix}>"

    # for immutability, disallow setting any value for the attributes.
    def __setattr__(self, *args):
        """Disables setting attributes 
        """
        raise TypeError(
            "DZPhoneNumber is an immutable object. You cannot set/delete its attributes"
        )

    __delattr__ = __setattr__
