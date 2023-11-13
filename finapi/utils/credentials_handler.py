import json
import os

from finapi.constants import CREDENTIALS_JSON, DEVICE_ID


def get_credentials() -> str:
    email = os.getenv("email")
    password = os.getenv("password")

    if email and password:
        credentials = {"email": email, "password": password}
    else:
        credential_file = open(CREDENTIALS_JSON, "r")
        credentials = json.load(credential_file)
    credentials["device_id"] = DEVICE_ID

    return json.dumps(credentials)


def get_credentials_mfa(mfa_code: str, otp_relay_token: str) -> str:
    data = {
        "device_id": DEVICE_ID,
        "otp_code": mfa_code,
        "otp_relay_token": otp_relay_token,
    }
    return json.dumps(data)
