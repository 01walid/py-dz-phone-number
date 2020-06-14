import random
import string

import pytest

from dz_phone_number import LandlinePrefix, MobileOperator


@pytest.fixture(scope="session")
def invalid_phone_numbers():
    return [
        "ABCD",
        "123456",
        # Statisfies the length for mobile
        "1234567890",
        "+111234567890",
        "00111234567890",
        # Statisfies the length for a landline
        "123456789",
        "+11123456789",
        "0011123456789",
        # Is valid but not Algerian number
        # Valid mobile
        "+216512345678",
        "00216512345678",
        # Valid Landline
        "0021638123456",
        "+21638123456",
        # has spaces
        # non-string
        213512345678,
        # empty string
        "",
        # Is None
        None,
        # too many ( or )
        "+ (213) (5) 12345678",
        "+ (213) (5) 12345678)",
        "+ (213) (5) 12345(67)(8)",
        # over dashed
        "+ (213) 512-34-56--78-",
        # starts with a dash
        "- (213) 512-34-56-78",
    ]


@pytest.fixture(scope="session")
def valid_phone_numbers():
    return [
        "0512345678",
        "0612345678",
        "0712345678",
        "00213512345678",
        "+213512345678",
        "+213 5 12 34 56 78",
        "+213-5-12-34-56-78",
        "(+213) 5-12-34-56-78",
        "+213 6 12 34 56 78",
        "+213-6-12-34-56-78",
        "(+213) 6-12-34-56-78",
        "+213 7 12 34 56 78",
        "+213-7-12-34-56-78",
        "(+213) 38-12-34-56",
        "0 38-12-34-56",
        "00213 38-12-34-56",
        "00213-38-12-34-56",
        "0-21-12-34-56",
    ]


@pytest.fixture(scope="session")
def valid_random_number():
    def rand_func():
        random_indicative = random.choice(["0", "+213", "00213", "(+213)", "(00213)"])
        numbers = random.choices(string.digits, k=random.choice([6, 8]))
        operator_or_region = (
            MobileOperator.all() if len(numbers) == 8 else LandlinePrefix.all()
        )

        operator_or_region = random.choice(operator_or_region)
        random_number = "".join(numbers)
        return f"{random_indicative}{operator_or_region}{random_number}"

    return rand_func
