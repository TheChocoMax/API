"""
Schemas for user registration requests.

This module defines the Pydantic model used for validating and serializing
user registration payloads in the authentication endpoints.
"""

from pydantic import BaseModel


class UserRegister(BaseModel):
    """
    Schema for user registration request.

    Attributes:
        token (str): The registration or invitation token.
        username (str): The desired username for the new user.
        password (str): The user's password.
        language_id (int | None): Optional language preference identifier.
    """

    token: str
    username: str
    password: str
    language_id: int | None = None
