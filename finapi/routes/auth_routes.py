from fastapi import APIRouter, HTTPException

from finapi.schemas.Login import Login
from finapi.services.auth_service import sign_in_request

router = APIRouter()


@router.post("/sign-in")
async def sign_in(credentials: Login):
    try:
        response = sign_in_request(credentials.mfa_code)
        if not response.success:
            raise HTTPException(response.status_code, response.message)
        else:
            return response
    except HTTPException as http_e:
        raise HTTPException(http_e.status_code, http_e.detail)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error | {e}")
