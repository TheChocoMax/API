"""
Email sending utilities.

This module provides functions for sending emails using FastAPI background tasks
and the FastMail library. It is used to send templated emails asynchronously
throughout the application.
"""

from fastapi import BackgroundTasks
from fastapi_mail import FastMail, MessageSchema, MessageType

from .config import conf
from .schemas import BaseEmailSchema


def send_email_background(background_tasks: BackgroundTasks, email: BaseEmailSchema):
    """
    Send an email in the background using FastAPI's BackgroundTasks.

    Args:
        background_tasks (BackgroundTasks): The FastAPI background task manager.
        email (BaseEmailSchema): The email payload containing recipients, subject, template, and body.

    This function creates a message from the provided schema and schedules it to be sent
    asynchronously using FastMail and the specified template.
    """
    message = MessageSchema(
        subject=email.subject,
        recipients=email.email,
        template_body=email.body,
        subtype=MessageType.html,
    )
    fm = FastMail(conf)
    background_tasks.add_task(
        fm.send_message, message, template_name=email.template_name
    )
