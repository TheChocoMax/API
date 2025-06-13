import pyotp
import pytest

from app.utility.security import verify_otp


@pytest.fixture
def totp_secret():
    return pyotp.random_base32()


@pytest.fixture
def hotp_secret():
    return pyotp.random_base32()


@pytest.fixture
def unsupported_secret():
    return pyotp.random_base32()


def test_verify_otp_valid_totp(totp_secret):
    totp = pyotp.TOTP(totp_secret)
    otp_code = totp.now()
    assert verify_otp(totp_secret, otp_code, "TOTP") is True


def test_verify_otp_invalid_totp(totp_secret):
    otp_code = "000000"
    assert verify_otp(totp_secret, otp_code, "TOTP") is False


def test_verify_otp_valid_hotp(hotp_secret):
    hotp = pyotp.HOTP(hotp_secret)
    counter = 0
    otp_code = hotp.at(counter)
    assert verify_otp(hotp_secret, otp_code, "HOTP", counter) is True


def test_verify_otp_invalid_hotp(hotp_secret):
    counter = 0
    otp_code = "000000"
    assert verify_otp(hotp_secret, otp_code, "HOTP", counter) is False


def test_verify_otp_unsupported_method(unsupported_secret):
    otp_code = "123456"
    assert verify_otp(unsupported_secret, otp_code, "SMS") is False


def test_verify_otp_invalid_secret():
    secret = "not_a_valid_secret"
    otp_code = "123456"
    assert verify_otp(secret, otp_code, "TOTP") is False


def test_verify_otp_invalid_code_type(totp_secret):
    otp_code = None
    assert verify_otp(totp_secret, otp_code, "TOTP") is False
