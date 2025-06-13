"""
Schemas for email-related payloads.

This module defines Pydantic models for validating and serializing
email payloads, such as registration and password reset emails,
used by the application's email utility functions.
"""

from typing import Any, Dict, List

from pydantic import BaseModel, EmailStr


class BaseEmailSchema(BaseModel):
    """
    Base schema for email payloads.

    Attributes:
        email (List[EmailStr]): List of recipient email addresses.
        subject (str): Subject line of the email.
        template_name (str): Name of the template to use for the email body.
        body (Dict[str, Any]): Data to render within the email template.
    """

    email: List[EmailStr]
    subject: str
    template_name: str
    body: Dict[str, Any]


class RegistrationEmailSchema(BaseEmailSchema):
    """
    Schema for registration confirmation emails.

    Attributes:
        subject (str): Default subject for registration emails.
        template_name (str): Default template for registration emails.
    """

    subject: str = "ChocoMax - Email Confirmation"
    template_name: str = "email_confirmation.html"


class PasswordResetEmailSchema(BaseEmailSchema):
    """
    Schema for password reset emails.

    Inherits all fields from BaseEmailSchema.
    """

    pass  # TODO
