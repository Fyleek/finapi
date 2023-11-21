from fastapi import APIRouter, HTTPException

from finapi.services import get_me_request

router = APIRouter()


@router.get("/me")
async def get_user_me():
    try:
        return get_me_request()
    except HTTPException as http_e:
        raise HTTPException(http_e.status_code, http_e.detail)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error | {e}")
