from pydantic import BaseModel


class Login(BaseModel):
    mfa_code: str
