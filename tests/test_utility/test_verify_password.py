import pytest
from argon2 import PasswordHasher

from app.utility.security import hash_password, verify_password

ph = PasswordHasher()


@pytest.fixture
def sample_password():
    """Fixture to provide a sample password for testing."""
    return "TestPass123!"


@pytest.fixture
def hashed_password(sample_password):
    """Fixture to provide a hashed password for testing."""
    return hash_password(sample_password)


@pytest.fixture
def wrong_password():
    """Fixture to provide a wrong password for testing."""
    return "WrongPass123!"


def test_verify_password(sample_password, hashed_password):
    """
    Test that the password verification works correctly.
    This ensures that the password can be hashed and then verified successfully.
    """
    assert verify_password(sample_password, hashed_password) is True


def test_verify_wrong_password(hashed_password, wrong_password):
    """
    Test that the password verification fails for a wrong password.
    This ensures that the verification function does not falsely accept incorrect passwords.
    """
    assert verify_password(wrong_password, hashed_password) is False


def test_verify_empty_password(hashed_password):
    """
    Test that the password verification fails for an empty password.
    This ensures that the verification function does not accept empty strings as valid passwords.
    """
    assert verify_password("", hashed_password) is False


def test_verify_password_tampered(sample_password, hashed_password):
    """
    Test that the password verification fails if the hash is tampered with.
    This ensures that the verification function detects modifications to the hash.
    """
    tampered_hash = hashed_password[:-5] + "xyz"  # Modify the hash slightly
    assert verify_password(sample_password, tampered_hash) is False
