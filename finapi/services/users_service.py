from finapi.constants import API_ROOT
from finapi.models.responses import FinaryResponse
from finapi.utils import get_session, get_request


def get_organizations_request() -> FinaryResponse:
    return get_request("users/me/organizations")
