import json
import os
from unittest.mock import mock_open

from finapi.constants import DEVICE_ID
from finapi.utils import get_credentials_mfa, get_credentials


def test_get_credentials_with_env_vars(mocker):
    mocker.patch.dict(os.environ, {"email": "test@example.com", "password": "secret"})

    result = get_credentials()

    result_dict = json.loads(result)

    expected = {"email": "test@example.com", "password": "secret", "device_id": f"{DEVICE_ID}"}

    assert result_dict == expected


def test_get_credentials_with_file(mocker):
    mocked_file_content = '{"email": "file@example.com", "password": "filesecret"}'

    mocker.patch("builtins.open", mock_open(read_data=mocked_file_content))

    mocker.patch.dict(os.environ, {"email": "", "password": ""}, clear=True)

    result = get_credentials()

    result_dict = json.loads(result)

    expected = {"email": "file@example.com", "password": "filesecret", "device_id": f"{DEVICE_ID}"}

    assert result_dict == expected


def test_get_credentials_mfa():
    mfa_code = "123456"
    opt_relay_token = "token123"

    result = get_credentials_mfa(mfa_code, opt_relay_token)

    result_dict = json.loads(result)

    expected = {"device_id": f"{DEVICE_ID}", "otp_code": "123456", "otp_relay_token": "token123"}

    assert result_dict == expected
