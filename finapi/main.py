from fastapi import FastAPI
from .routes import auth_router
from .routes import users_router
from .routes import organizations_router
#from .routes import bank_router

app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(users_router, prefix="/users", tags=["users"])
app.include_router(organizations_router, prefix="/organizations", tags=["organization"])
#app.include_router(bank_router, prefix="/bank", tags=["bank"])
