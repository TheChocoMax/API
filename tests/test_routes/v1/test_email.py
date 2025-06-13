from unittest.mock import AsyncMock, patch

import pytest
from fastapi.testclient import TestClient

from app.routes.v1.endpoints import email as email_module

EMAIL_PATH = "app.routes.v1.endpoints.email"


@pytest.fixture
def client():
    from fastapi import FastAPI

    app = FastAPI()
    app.include_router(email_module.router, prefix="/v1/email")
    return TestClient(app)


@pytest.fixture(autouse=True)
def patch_email_dependencies():
    with (
        patch(f"{EMAIL_PATH}.send_email_background") as send_mock,
        patch(f"{EMAIL_PATH}.hash_email", return_value="hashed-email") as hash_mock,
        patch(
            f"{EMAIL_PATH}.encrypt_email", return_value="encrypted-email"
        ) as enc_mock,
        patch(
            f"{EMAIL_PATH}.create_verification_token", return_value="test-token"
        ) as token_mock,
    ):
        yield {
            "send": send_mock,
            "hash": hash_mock,
            "enc": enc_mock,
            "token": token_mock,
        }


@pytest.fixture
def mock_db_and_override(client):
    mock_db = AsyncMock()

    async def override_get_db():
        yield mock_db

    client.app.dependency_overrides[email_module.get_db] = override_get_db
    return mock_db


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "email",
    [
        "user@example.com",
        "USER@domain.io",
        "test.user+alias@domain.co.uk",
        "first.last@sub.domain.com",
        "user123@domain.io",
        "user_name@domain.org",
    ],
)
async def test_send_confirmation_email_success(
    client: TestClient,
    patch_email_dependencies: dict,
    mock_db_and_override: AsyncMock,
    email: str,
):
    mock_db = mock_db_and_override

    response = client.post("/v1/email/confirmation", json={"email": email})

    assert response.status_code == 200
    data = response.json()
    assert data["detail"] == "Confirmation email sent"

    patch_email_dependencies["token"].assert_called_once()
    patch_email_dependencies["enc"].assert_called_once_with(email)
    patch_email_dependencies["hash"].assert_called_once_with(email)
    patch_email_dependencies["send"].assert_called_once()
    mock_db.execute.assert_awaited_once()
    mock_db.commit.assert_awaited_once()


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "email",
    [
        "",
        "not-an-email",
        "user@.com",
        "user@domain",
        "userdomain.com",
        "@domain.com",
        "user@domain..com",
        "user@domain,com",
        "user@domain.?com",
    ],
)
async def test_send_confirmation_email_failure(
    client: TestClient,
    patch_email_dependencies: dict,
    mock_db_and_override: AsyncMock,
    email: str,
):
    mock_db = mock_db_and_override

    response = client.post("/v1/email/confirmation", json={"email": email})
    assert response.status_code == 422  # Unprocessable Entity

    patch_email_dependencies["token"].assert_not_called()
    patch_email_dependencies["enc"].assert_not_called()
    patch_email_dependencies["hash"].assert_not_called()
    patch_email_dependencies["send"].assert_not_called()
    mock_db.execute.assert_not_awaited()
    mock_db.commit.assert_not_awaited()
