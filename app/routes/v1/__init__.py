"""
Base module for the API version 1 routes.
"""

from fastapi import FastAPI

from .endpoints.authentication import router as auth_router
from .endpoints.email import router as email_router
from .endpoints.orders import router as order_router
from .endpoints.products import router as product_router

__version__ = "1.2.0"

api = FastAPI(title="ChocoMax Shop API", version=__version__)

api.include_router(auth_router, prefix="/auth", tags=["Authentication"])
api.include_router(email_router, prefix="/email", tags=["Email"])
api.include_router(product_router, prefix="/products", tags=["Products"])
api.include_router(order_router, prefix="/orders", tags=["Orders"])
