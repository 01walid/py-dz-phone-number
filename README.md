# [WIP] Algerian phone numbers as a value object


Inspired from [the PHP implementation](https://github.com/cherifGsoul/php-algerian-mobile-phone-number) with some differences (see below).

------------

Algerian phone numbers as a value object implementation in Python. This can be used in your domain models or be integrated with your favorite framework.

What is value object?
> In computer science, a value object is a small object that represents a simple entity whose equality is not based on identity: i.e. two value objects are equal when they have the same value, not necessarily being the same object.

Read more on [wikipedia](https://en.wikipedia.org/wiki/Value_object).

## Installation:

```
pip install dz-phone-numbers
```

## Usage:

```python
from dz_phone_number import DZPhoneNumber

dz_phone_number = DZPhoneNumber("0599000000") # or DZPhoneNumber.from_string("0599000000")
dz_phone_number.is_mobile() # True
dz_phone_number.is_landline() # a.k.a Fixe. False
dz_phone_number.is_ooredoo() # True
dz_phone_number.is_djezzy() # false
```

### equality
```python
DZPhoneNumber("0599000000") == DZPhoneNumber("+213 599000000") # True
DZPhoneNumber("(0) 599000000") == DZPhoneNumber("0 599-00-00-00") # True
DZPhoneNumber("(0) 599000000") == DZPhoneNumber("(0) 699000000"") # False
```

### Correctness 
```Python
try:
    DZPhoneNumber("InvalidNumber")
except ValueError: # ValueError can catch it
    pass
# otherwise you can also except `InvalidDZPhoneNumber` 
```


# Differences from the PHP implementation (as of writing this):
- This raises a `ValueError` (Python built-in) instead of the broad `Exception` `InvalidDZPhoneNumber` is an alias of `ValueError`.
- A different version of regex with support for landline (a.k.a fixe) numbers.
- Enums are used to both limit landline possible values, and make it extensible (e.g. very easy if, say, a new operator got into Algeria).
- This uses Python regex "capturing groups" feature. Where "Country Code", "Operator or Region" and the "Number" are put in groups when matched.
- pytest are used instead of any other spec or behavior testing.
- Immutability is achieved through `__slots__` and overriding `__setattr__` and `__delattr__`. This was a bit more flexibile that `@dataclass(frozen=True)`.
