"""
Schemas for email-related API requests.

This module defines the Pydantic model used for validating and serializing
email request payloads in the API v1 endpoints.
"""

from pydantic import BaseModel, EmailStr


class EmailRequest(BaseModel):
    """
    Schema for email-related API requests.

    Attributes:
        email (EmailStr): The user's email address.
    """

    email: EmailStr
