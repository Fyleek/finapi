import json

import pytest
from unittest import mock

from finapi.constants import API_ROOT
from finapi.services import sign_in_request


@pytest.fixture
def mock_dependencies():
    with mock.patch("finapi.services.auth_service.get_credentials") as mock_get_credentials, \
            mock.patch("finapi.services.auth_service.get_header_login") as mock_get_header_login, \
            mock.patch("finapi.services.auth_service.get_session") as mock_get_session, \
            mock.patch("http.cookiejar.MozillaCookieJar") as mock_cookie_jar, \
            mock.patch("finapi.services.auth_service.logging") as mock_logging, \
            mock.patch("finapi.services.auth_service.get_credentials_mfa") as mock_get_credentials_mfa:
        mock_session = mock.Mock()
        mock_get_session.return_value = mock_session
        yield mock_get_credentials, \
            mock_get_header_login, \
            mock_session, \
            mock_cookie_jar, \
            mock_logging, \
            mock_get_credentials_mfa


def test_sign_in_success_no_mfa(mock_dependencies):
    mock_get_credentials, \
        mock_get_header_login, \
        mock_session, \
        mock_cookie_jar, \
        mock_logging, \
        mock_get_credentials_mfa = mock_dependencies

    # Simulate a 201 response for MFA POST request
    response_201 = mock.Mock()
    response_201.status_code = 201

    # Mock configuration
    mock_get_credentials.return_value = "credentials"
    mock_get_header_login.return_value = "headers"
    mock_session.post.return_value = mock.Mock(status_code=response_201.status_code)

    #  Function call
    response = sign_in_request("")

    # Assertions
    assert response.success
    assert response.status_code == 200
    assert response.message == "Sign-in done"
    assert response.data is None
    assert response.data is None
    mock_cookie_jar.return_value.save.assert_called_once()
    mock_logging.info.assert_has_calls([
        mock.call(f"{API_ROOT}/auth/signin was executed | Status-Code:{response_201.status_code}"),
        mock.call("Sign-in NO MFA OK")
    ])


def test_sign_in_success_mfa(mock_dependencies):
    mock_get_credentials, \
        mock_get_header_login, \
        mock_session, \
        mock_cookie_jar, \
        mock_logging, \
        mock_get_credentials_mfa = mock_dependencies
    mfa_code = "123456"
    otp_relay_token = "relay_token"
    mfa_data = json.dumps({
        "device_id": "iphone",
        "otp_code": mfa_code,
        "otp_relay_token": otp_relay_token,
    })

    # Mock configuration
    mock_get_credentials.return_value = "credentials"
    mock_get_header_login.return_value = {}
    mock_get_credentials_mfa.return_value = mfa_data

    # Simulate a 202 response for the first POST request
    response_202 = mock.Mock()
    response_202.status_code = 202
    response_202.json.return_value = {"result": {"otp_relay_token": otp_relay_token}}

    # Simulate a 201 response for MFA POST request
    response_201 = mock.Mock()
    response_201.status_code = 201

    # Configure the mock session to return mock responses
    mock_session.post.side_effect = [response_202, response_201]

    # Function call
    response = sign_in_request(mfa_code)

    # Assertions
    assert response.success
    assert response.status_code == 200
    assert response.message == "Sign-in done"
    assert response.data is None
    assert response.data is None
    mock_cookie_jar.return_value.save.assert_called_once()
    mock_logging.info.assert_called_with("Sign-in MFA OK")
    mock_session.post.assert_has_calls([
        mock.call(f"{API_ROOT}/auth/signin", "credentials", headers={"Content-Length": f"{len(mfa_data)}"}),
        mock.call(f"{API_ROOT}/auth/signin", mfa_data, headers={"Content-Length": f"{len(mfa_data)}"})
    ])


def test_sign_in_failed_no_mfa(mock_dependencies):
    mock_get_credentials, \
        mock_get_header_login, \
        mock_session, \
        mock_cookie_jar, \
        mock_logging, \
        mock_get_credentials_mfa = mock_dependencies

    # Mock configuration
    mock_get_credentials.return_value = "credentials"
    mock_get_header_login.return_value = "headers"

    # Simulate failure response for POST request
    failure_status_code = 400
    failure_reason = "Bad Request"
    mock_session.post.return_value = mock.Mock(status_code=failure_status_code, reason=failure_reason)

    # Function call
    response = sign_in_request("")

    # Assertions
    assert not response.success
    assert response.status_code == 400
    assert response.detail == failure_reason
    assert response.data is None
    mock_session.post.assert_called_once_with(f"{API_ROOT}/auth/signin", "credentials", headers="headers")
    mock_logging.info(f"{API_ROOT}/auth/signin was executed | Status-Code:{response.status_code}")
    mock_logging.error(f"Sign-in NO MFA OK | ERROR-CODE:{failure_status_code}")
    #  TODO: failed no mfa
