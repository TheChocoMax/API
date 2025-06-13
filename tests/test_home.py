"""
Test the home endpoint of the API.
"""

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.routes.home import router as home_router


@pytest.fixture
def client():
    """Fixture to create a test client for the FastAPI app with only the home router."""
    app = FastAPI()
    app.include_router(home_router)
    return TestClient(app)


def test_home(client):
    """Test the home endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the ChocoMax Shop API!"}
