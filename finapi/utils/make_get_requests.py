from finapi.constants import API_ROOT
from finapi.models import FinaryResponse
from finapi.utils import get_session


def get_request(endpoint: str) -> FinaryResponse:
    session = get_session()
    response = session.get(f"{API_ROOT}/{endpoint}")
    status_code = response.status_code
    response_json = response.json()
    return FinaryResponse(
        response_json.get("result"),
        response_json.get("message"),
        response_json.get("error"),
        status_code,
    ).response()
