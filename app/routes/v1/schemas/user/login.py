"""
Schemas for user login and two-factor authentication (2FA) requests.

This module defines Pydantic models used for validating and serializing
user login and 2FA payloads in the authentication endpoints.
"""

from pydantic import BaseModel


class UserLogin(BaseModel):
    """
    Schema for user login request.

    Attributes:
        email (str): The user's email address.
        password (str): The user's password.
    """

    email: str
    password: str


class UserLogin2FA(BaseModel):
    """
    Schema for user two-factor authentication (2FA) request.

    Attributes:
        otp_code (int): The one-time password code for 2FA.
        token (str): The temporary token issued after initial login.
    """

    otp_code: int
    token: str
