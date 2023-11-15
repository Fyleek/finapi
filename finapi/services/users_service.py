import http.cookiejar

from finapi.constants import API_ROOT, COOKIE_FILE
from finapi.models.responses import FinaryResponse
from finapi.utils import get_session


def get_organizations_request() -> FinaryResponse:
    organizations_url = f"{API_ROOT}/users/me/organizations"
    cookies = http.cookiejar.MozillaCookieJar(COOKIE_FILE)
    session = get_session(cookies)
    response = session.get(organizations_url).json()
    return FinaryResponse(
        response.get("result"),
        response.get("message"),
        response.get("status_code"),
        response.get("error"),
    ).response()
