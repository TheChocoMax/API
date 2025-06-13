"""
Test suite for the v1 `/orders` endpoint of the ChocoMax API.

This module uses the `v1_get` utility to avoid repeating the API version path.
"""

import pytest
from fastapi.testclient import TestClient

from app.routes.v1.endpoints import orders as orders_module


@pytest.fixture
def client():
    from fastapi import FastAPI

    app = FastAPI()
    app.include_router(orders_module.router, prefix="/v1/orders")
    return TestClient(app)


def test_orders(client: TestClient):
    """
    Test that the `/api/v1/orders` endpoint returns a 200 status
    and responds with a JSON list.
    """
    response = client.get("/v1/orders")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
