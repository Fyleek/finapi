from .auth_routes import router as auth_router
from .users_routes import router as users_router

__all__ = ["auth_router", "users_router"]

__author__ = "Fyleek"
__description__ = "Defines API routes and endpoints"
__copyright__ = "Copyright 2023, Fyleek"
__licence__ = "MIT"
