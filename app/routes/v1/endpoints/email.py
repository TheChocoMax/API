"""
Email endpoints for user confirmation.

This module provides FastAPI endpoints for sending confirmation emails to users.
It handles the creation of verification tokens, email encryption, and interaction
with the database to register pending users.
"""

from fastapi import APIRouter, BackgroundTasks, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.routes.v1.schemas.email.request import EmailRequest
from app.utility.database import get_db
from app.utility.email.schemas import RegistrationEmailSchema
from app.utility.email.sender import send_email_background
from app.utility.security import create_verification_token, encrypt_email, hash_email

router = APIRouter()


@router.post("/confirmation")
async def send_confirmation_email(
    data: EmailRequest,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db),
):
    """
    Endpoint to send a confirmation email to the user.

    This endpoint accepts a POST request with the user's email in the body,
    generates a verification token, encrypts and hashes the email, sends a
    confirmation email asynchronously, and stores the pending user in the database.

    Args:
        data (EmailRequest): The request payload containing the user's email.
        background_tasks (BackgroundTasks): FastAPI background task manager.
        db (AsyncSession): The database session.

    Returns:
        dict: A dictionary with a detail message and the confirmation token.
    """
    email = data.email
    token = create_verification_token()
    email_encrypted = encrypt_email(email)
    email_hash = hash_email(email)

    email_schema = RegistrationEmailSchema(
        email=[email],
        body={
            "title": "Welcome to ChocoMax",
            "confirmation_url": f"http://<chocomax-domain>?token={token}",
        },
    )

    send_email_background(background_tasks, email_schema)

    # Send the token to the Database
    await db.execute(
        text("CALL create_pending_user(:email_encrypted, :email_hash, :token)"),
        {"email_encrypted": email_encrypted, "email_hash": email_hash, "token": token},
    )
    await db.commit()

    return {"detail": "Confirmation email sent"}
