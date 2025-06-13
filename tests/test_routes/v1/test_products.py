"""
Test suite for the v1 `/products` endpoint of the ChocoMax API.

This module uses the `v1_get` utility to avoid repeating the API version path.
"""

import pytest
from fastapi.testclient import TestClient

from app.routes.v1.endpoints import products as products_module


@pytest.fixture
def client():
    from fastapi import FastAPI

    app = FastAPI()
    app.include_router(products_module.router, prefix="/v1/products")
    return TestClient(app)


def test_products(client: TestClient):
    """
    Test that the `/api/v1/products` endpoint returns a 200 status
    and responds with a JSON list.
    """
    response = client.get("/v1/products")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
