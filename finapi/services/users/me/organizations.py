from finapi.schemas import FinaryResponse
from finapi.utils import get_request


def get_my_organizations_request() -> FinaryResponse:
    return get_request("users/me/organizations")
