import pytest
from fastapi import HTTPException

from finapi.models import FinapiResponse


def test_auth_service_response_constructor():
    # Test with all parameters
    response = FinapiResponse(True, {"key": "value"}, "Message", 200)
    assert response.success is True
    assert response.data == {"key": "value"}
    assert response.message == "Message"
    assert response.status_code == 200

    # Test with default parameters
    response = FinapiResponse()
    assert response.success is None
    assert response.data is None
    assert response.message == ""
    assert response.status_code == 0


def test_auth_service_response_success():
    # Test with default parameters
    response = FinapiResponse.success(None)
    assert response.get("success") is True
    assert response.get("data") is None
    assert response.get("message") == "Success"
    assert response.get("status_code") == 200

    # Test with custom parameters
    response = FinapiResponse.success({"key": "value"}, "Custom message", 201)
    assert response.get("success") is True
    assert response.get("data") == {"key": "value"}
    assert response.get("message") == "Custom message"
    assert response.get("status_code") == 201


def test_auth_service_response_error():
    # Test with default parameters
    with pytest.raises(HTTPException) as exc:
        FinapiResponse.error()
    assert exc.value.headers is None
    assert exc.value.detail == "Internal Server Error"
    assert exc.value.status_code == 500

    # Test with custom parameters
    with pytest.raises(HTTPException) as exc:
        FinapiResponse.error(404, "Not found")
    assert exc.value.headers is None
    assert exc.value.detail == "Not found"
    assert exc.value.status_code == 404
