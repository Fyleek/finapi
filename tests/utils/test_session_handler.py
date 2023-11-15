from unittest import mock

from finapi.constants import COOKIE_FILE
from finapi.utils import get_session


@mock.patch("http.cookiejar.MozillaCookieJar")
@mock.patch("requests.Session")
def test_get_session(mock_requests_session, mock_mozilla_cookie_jar):
    # Mock configuration for MozillaCookieJar
    mock_cookie_jar_instance = mock_mozilla_cookie_jar.return_value
    mock_cookie_jar_instance.load.return_value = "Cookies 🍪"

    # Function call
    session = get_session()

    # Assertions
    mock_requests_session.assert_called_once()
    mock_mozilla_cookie_jar.assert_called_once_with(COOKIE_FILE)
    mock_cookie_jar_instance.load.assert_called_once()
    assert session.cookies == mock_cookie_jar_instance
