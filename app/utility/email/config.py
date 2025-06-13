"""
Email configuration module.

This module loads environment variables and sets up the email connection
configuration for sending emails through the application.
"""

import os
from pathlib import Path

from dotenv import load_dotenv
from fastapi_mail import ConnectionConfig

load_dotenv(".env")

conf = ConnectionConfig(
    MAIL_USERNAME=os.getenv("MAIL_USERNAME", "user@example.com"),
    MAIL_PASSWORD=os.getenv("MAIL_PASSWORD", "password"),
    MAIL_FROM=os.getenv("MAIL_FROM", "noreply@chocomax.com"),
    MAIL_PORT=os.getenv("MAIL_PORT", "587"),
    MAIL_SERVER=os.getenv("MAIL_SERVER", "smtp.example.com"),
    MAIL_FROM_NAME=os.getenv("MAIL_FROM_NAME", "ChocoMax"),
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
    TEMPLATE_FOLDER=Path(__file__).parent.parent.parent / "templates",
)
