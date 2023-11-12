from typing import Dict


class AuthServiceResponse:
    def __init__(
        self,
        success: bool,
        data: Dict | None = None,
        detail: str | None = "",
        message: str = "",
        status_code: int = 0,
    ):
        self.success = success
        self.data = data
        self.detail = detail
        self.message = message
        self.status_code = status_code

    @staticmethod
    def success(data=None, detail=None, message: str = "Success", status_code: int = 200):
        return AuthServiceResponse(True, data, detail, message, status_code)

    @staticmethod
    def error(
        status_code: int = 500,
        detail: str = "Unknown detail",
        message: str = "Unknown message",
    ):
        return AuthServiceResponse(False, None, detail, message, status_code)
