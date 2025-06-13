"""
This module defines the SQLAlchemy ORM model for the 'users' table.

It provides the User class, which stores user authentication and profile information,
including encrypted and hashed email/phone fields, password hash, language preference,
and timestamps for creation, updates, login, and deletion.
"""

import uuid
from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer, Text
from sqlalchemy.dialects.postgresql import UUID

from app.models import Base


class User(Base):
    """
    SQLAlchemy ORM model for the 'users' table.

    Stores user authentication and profile information, including encrypted and hashed
    email/phone fields, password hash, language preference, and timestamps for
    creation, updates, login, and deletion.

    Attributes:
        user_id (UUID): Primary key, unique user identifier.
        username (str): Unique username for the user.
        email_encrypted (str): AES-encrypted email address.
        email_hash (str): SHA-256 hash of the normalized email.
        is_email_verified (bool): Whether the user's email is verified.
        password_hash (str): Argon2 hash of the user's password.
        phone_encrypted (str): AES-encrypted phone number.
        phone_hash (str): SHA-256 hash of the normalized phone number.
        language_id (int): Preferred language ID.
        created_at (datetime): Timestamp of user creation.
        updated_at (datetime): Timestamp of last update.
        last_login_at (datetime): Timestamp of last login.
        deleted_at (datetime): Timestamp of deletion (soft delete).
    """

    __tablename__ = "users"
    __table_args__ = {"extend_existing": True}

    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    username = Column(Text, unique=True, nullable=False)

    email_encrypted = Column(Text, nullable=False)
    email_hash = Column(Text, unique=True, nullable=False)
    is_email_verified = Column(Boolean, default=False)

    password_hash = Column(Text, nullable=False)

    phone_encrypted = Column(Text)
    phone_hash = Column(Text, unique=True)

    language_id = Column(Integer, nullable=True)

    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    last_login_at = Column(DateTime(timezone=True))
    deleted_at = Column(DateTime(timezone=True))
