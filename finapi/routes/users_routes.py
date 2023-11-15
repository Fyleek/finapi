from fastapi import APIRouter, HTTPException

from finapi.services import get_organizations_request

router = APIRouter()


@router.get("/organizations")
async def get_organizations():
    try:
        return get_organizations_request()
    except HTTPException as http_e:
        raise HTTPException(http_e.status_code, http_e.detail)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error | {e}")
