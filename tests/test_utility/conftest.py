import pytest


@pytest.fixture
def sample_email():
    """Fixture to provide a sample email for testing."""
    return "user@example.com"


@pytest.fixture
def sample_phone():
    """Fixture to provide a sample phone number for testing."""
    return "+1234567890"
