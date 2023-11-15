from typing import Dict, Any

from fastapi import HTTPException


class FinapiResponse:
    def __init__(
        self,
        success: bool | None = None,
        data: Any = None,
        message: str = "",
        status_code: int = 0,
    ):
        self.success = success
        self.data = data
        self.message = message
        self.status_code = status_code

    @staticmethod
    def success(
        data: Any = None, message: str = "Success", status_code: int = 200
    ) -> Dict[str, Any]:
        return {"success": True, "message": message, "data": data, "status_code": status_code}

    @staticmethod
    def error(status_code: int = 500, message: str = "Internal Server Error"):
        raise HTTPException(status_code=status_code, detail=message)
