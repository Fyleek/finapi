from finapi.models import AuthServiceResponse


def test_auth_service_response_constructor():
    # Test with all parameters
    response = AuthServiceResponse(True, {"key": "value"}, "Detail", "Message", 200)
    assert response.success is True
    assert response.data == {"key": "value"}
    assert response.detail == "Detail"
    assert response.message == "Message"
    assert response.status_code == 200

    # Test with default parameters
    response = AuthServiceResponse(False)
    assert response.success is False
    assert response.data is None
    assert response.detail == ""
    assert response.message == ""
    assert response.status_code == 0

def test_auth_service_response_success():
    # Test with default parameters
    response = AuthServiceResponse.success()
    assert response.success is True
    assert response.data is None
    assert response.detail is None
    assert response.message == "Success"
    assert response.status_code == 200

    # Test with custom parameters
    response = AuthServiceResponse.success({"key": "value"}, "Detail", "Custom message", 201)
    assert response.success is True
    assert response.data == {"key": "value"}
    assert response.detail == "Detail"
    assert response.message == "Custom message"
    assert response.status_code == 201

def test_auth_service_response_error():
    # Test with default parameters
    response = AuthServiceResponse.error()
    assert response.success is False
    assert response.data is None
    assert response.detail == "Unknown detail"
    assert response.message == "Unknown message"
    assert response.status_code == 500

    # Test with custom parameters
    response = AuthServiceResponse.error(404, "Not found", "Custom error message")
    assert response.success is False
    assert response.data is None
    assert response.detail == "Not found"
    assert response.message == "Custom error message"
    assert response.status_code == 404
