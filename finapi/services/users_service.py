from finapi.constants import API_ROOT
from finapi.models.responses import FinaryResponse
from finapi.utils import get_session


def get_organizations_request() -> FinaryResponse:
    organizations_url = f"{API_ROOT}/users/me/organizations"
    session = get_session()
    response = session.get(organizations_url)
    status_code = response.status_code
    response_json = response.json()
    return FinaryResponse(
        response_json.get("result"),
        response_json.get("message"),
        response_json.get("error"),
        status_code
    ).response()
