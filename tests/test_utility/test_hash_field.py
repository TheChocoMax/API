import re

import pytest

from app.utility.security import hash_email, hash_phone


@pytest.fixture
def hashed_email(sample_email):
    """Fixture to provide a hashed email for testing."""
    return hash_email(sample_email)


@pytest.fixture
def hashed_phone(sample_phone):
    """Fixture to provide a hashed phone number for testing."""
    return hash_phone(sample_phone)


def test_hash_field_type(hashed_email, hashed_phone):
    """
    Test that the hashed fields are of type str.
    This ensures that the hash function returns a string.
    """
    assert isinstance(hashed_email, str)
    assert isinstance(hashed_phone, str)


def test_hash_field_length(hashed_email, hashed_phone):
    """
    Test that the hashed fields are precisely 64 characters long.
    This is the expected length for SHA-256 hashes.
    """
    assert len(hashed_email) == 64
    assert len(hashed_phone) == 64


def test_hash_field_format(hashed_email, hashed_phone):
    """
    Test that the hashed fields are in the expected format.
    Hashed fields should be hexadecimal strings.
    """
    assert re.match(r"^[0-9a-f]{64}$", hashed_email)
    assert re.match(r"^[0-9a-f]{64}$", hashed_phone)
