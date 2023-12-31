from fastapi import APIRouter, HTTPException

from finapi.schemas.Login import Login
from finapi.services.auth import sign_in_request

router = APIRouter()


@router.post("/sign-in")
async def sign_in(credentials: Login):
    try:
        return sign_in_request(credentials.mfa_code)
    except HTTPException as http_e:
        raise HTTPException(http_e.status_code, http_e.detail)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error | {e}")
