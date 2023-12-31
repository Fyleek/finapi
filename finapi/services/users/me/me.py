from finapi.schemas import FinaryResponse
from finapi.utils import get_request


def get_me_request() -> FinaryResponse:
    return get_request("users/me")
