from fastapi import APIRouter, HTTPException

from finapi.services import users

router = APIRouter()


@router.get("/me")
async def get_me():
    try:
        return users.get_me_request()
    except HTTPException as http_e:
        raise HTTPException(http_e.status_code, http_e.detail)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error | {e}")


@router.get("/me/organizations")
async def get_my_organizations():
    try:
        return users.get_my_organizations_request()
    except HTTPException as http_e:
        raise HTTPException(http_e.status_code, http_e.detail)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error | {e}")


@router.get("/me/subscriptions")
async def get_my_subscriptions():
    try:
        return users.get_subscription_details_request()
    except HTTPException as http_e:
        raise HTTPException(http_e.status_code, http_e.detail)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error | {e}")
