import re

import pytest

from app.utility.security import decrypt_field, encrypt_email, encrypt_phone


@pytest.fixture
def encrypted_email(sample_email):
    """Fixture to provide an encrypted email for testing."""
    return encrypt_email(sample_email)


@pytest.fixture
def encrypted_phone(sample_phone):
    """Fixture to provide an encrypted phone number for testing."""
    return encrypt_phone(sample_phone)


def test_encrypt_field_type(encrypted_email, encrypted_phone):
    """
    Test that the encrypted fields are of type str.
    This ensures that the encryption function returns a string.
    """
    assert encrypted_email.isascii()
    assert encrypted_phone.isascii()


def test_encrypt_field_length(encrypted_email, encrypted_phone):
    """
    Test that the encrypted fields are not empty.
    This ensures that the encryption does not produce empty strings.
    """
    assert len(encrypted_email) > 0
    assert len(encrypted_phone) > 0


def test_encrypt_field_format(encrypted_email, encrypted_phone):
    """
    Test that the encrypted fields are in the expected format.
    Encrypted fields should be base64 encoded strings.
    """
    assert re.match(r"^[A-Za-z0-9+/=]+$", encrypted_email)
    assert re.match(r"^[A-Za-z0-9+/=]+$", encrypted_phone)


def test_decrypt_email(sample_email, encrypted_email):
    assert decrypt_field(encrypted_email) == sample_email


def test_decrypt_phone(sample_phone, encrypted_phone):
    assert decrypt_field(encrypted_phone) == sample_phone
