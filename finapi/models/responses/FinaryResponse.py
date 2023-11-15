from typing import Dict, List

from .FinapiResponse import FinapiResponse


class FinaryResponse(FinapiResponse):
    def __init__(
        self,
        result: Dict | List | None = None,
        message: str = "",
        error: bool | None = None,
        status_code: int = 0,
    ):
        super().__init__(data=result, message=message, status_code=status_code)
        self.result = result
        self.message = message
        self.error = error
        self.status_code = status_code

    def response(self):
        if self.error:
            return FinapiResponse.error(self.status_code, self.message)
        else:
            return FinapiResponse.success(self.result, self.message, self.status_code)
