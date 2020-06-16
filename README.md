# Algerian phone numbers as a value object


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
dz_phone_number.indicative # <CountryCode.LOCAL: '0'>
dz_phone_number.operator_or_region # <MobileOperator.OOREDOO: 5>
dz_phone_number.suffix # '99000000'

dz_phone_number.is_mobile() # True
dz_phone_number.is_landline() # a.k.a Fixe. False
dz_phone_number.is_ooredoo() # True
dz_phone_number.is_djezzy() # false
dz_phone_number.is_annaba() # false

DZPhoneNumber("038123456").is_annaba() # True

# repr:
<DZPhoneNumber:CountryCode.LOCAL - MobileOperator: OOREDOO - 99000000>

# str:
str(dz_phone_number) # 0599000000
```

### Equality

```python
DZPhoneNumber("0599000000") == DZPhoneNumber("+213 599000000") # True
DZPhoneNumber("(0) 599000000") == DZPhoneNumber("0 599-00-00-00") # True
DZPhoneNumber("(0) 599000000") == DZPhoneNumber("(0) 699000000"") # False
```

### Correctness 

```Python
try:
    DZPhoneNumber("09 12 34 56 78")
except ValueError: # ValueError can catch it
    pass
# Otherwise you can also expect `InvalidDZPhoneNumber` (an alias of ValueError).
```
### Immutability

The object can't be modified if you try to modify of its members, a `TypeError` will be raised:
```python
dz_phone_number.number = '038123456' # will raise TypeError.
```

# Understanding the regex 
03 main parts of the full number are categorized into three groups: indicative (Country Code), Operator or Region (e.g. Ooredoo or Annaba), and the rest of the dial number.

<p align="center">
    <img src="https://res.cloudinary.com/walid/image/upload/v1592310084/regex-explain1_ggau8t.png" />
</p>

The regex uses Python's [capturing group](https://docs.python.org/3/howto/regex.html#grouping) feature built in its regex engine. Where "Country Code", "Operator or Region" and the "Number" are put into numbered groups when matched.

The regex also uses a conditional statemet in the form of `(?(1)yes|no)` where `(1)` is the capturing group number. The following picture explain how it's working:

<p align="center">
    <img src="https://res.cloudinary.com/walid/image/upload/v1592310151/regex-explain2_hmvwgp.png" />
</p>

## Differences from the PHP implementation (as of writing this):
- This raises a `ValueError` (Python built-in) instead of the broad `Exception` `InvalidDZPhoneNumber` is an alias of `ValueError`.
- A different version of regex with support for landline (a.k.a fixe) numbers.
- Enums are used to both limit landline possible values, and make it extensible (e.g. very easy if, say, a new operator got into Algeria).
- This uses Python regex "capturing groups" feature. Where "Country Code", "Operator or Region" and the "Number" are put in groups when matched.
- pytest are used instead of any other spec or behavior testing.
- Immutability is achieved through `__slots__` and overriding `__setattr__` and `__delattr__`. This was a bit more flexibile that `@dataclass(frozen=True)`.

# Bonuses 

This is a simple, self-contained problem. One of the reasons I wrote this is to serve as a python package example for the Algerian Python community where:
- The code is [Black](https://github.com/psf/black)-formatted. 
- Type annotated code using Python type hints. Checked with [MyPy](http://mypy-lang.org/).
- The project structure follows what's common for Python projects. See the [Hitchhiker guide](https://docs.python-guide.org/writing/structure/).
- A simple `Makefile` within to show how to build this (with Python wheels support) and how to release a package to pypi. Just issue `make` to see the available commands.
- Example `setup.py`
- Testing with pytest.
