from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient

from app.routes.v1.endpoints import authentication as auth_module

AUTH_PATH = "app.routes.v1.endpoints.authentication"


@pytest.fixture
def client():
    from fastapi import FastAPI

    app = FastAPI()
    app.include_router(auth_module.router, prefix="/v1/auth")
    return TestClient(app)
