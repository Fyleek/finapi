import pytest
from unittest import mock

from finapi.models import AuthServiceResponse
from finapi.services import sign_in_request


@pytest.fixture
def mock_dependencies():
    with mock.patch("finapi.services.auth_service.get_credentials") as mock_get_credentials, \
            mock.patch("finapi.services.auth_service.get_header_login") as mock_get_header_login, \
            mock.patch("finapi.services.auth_service.get_session") as mock_get_session, \
            mock.patch("http.cookiejar.MozillaCookieJar") as mock_cookie_jar, \
            mock.patch("finapi.services.auth_service.logging") as mock_logging:
        mock_session = mock.Mock()
        mock_get_session.return_value = mock_session
        yield mock_get_credentials, mock_get_header_login, mock_session, mock_cookie_jar, mock_logging


def test_sign_in_success_no_mfa(mock_dependencies):
    mock_get_credentials, mock_get_header_login, mock_session, mock_cookie_jar, mock_logging = mock_dependencies
    mock_get_credentials.return_value = "credentials"
    mock_get_header_login.return_value = "headers"
    mock_session.post.return_value = mock.Mock(status_code=201)

    response = sign_in_request("mfa_code")

    assert response.success
    assert response.status_code == 200
    assert response.message == "Sign-in done"
    assert response.data is None
    assert response.data is None
    mock_cookie_jar.return_value.save.assert_called_once()
    mock_logging.info.assert_called_with("Sign-in NO MFA OK")

    #  TODO: success mfa
    #  TODO: failed no mfa
    #  TODO: failed no mfa
