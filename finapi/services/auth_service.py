import http.cookiejar
import json
import logging

from finapi.constants import API_ROOT, COOKIE_FILE
from finapi.models import FinapiResponse
from finapi.utils.credentials_handler import get_credentials, get_credentials_mfa
from finapi.utils.header_handler import get_header_login
from finapi.utils.session_handler import get_session


def sign_in_request(mfa_code: str):
    signin_url = f"{API_ROOT}/auth/signin"

    credentials = get_credentials()
    headers = get_header_login(credentials)
    cookies = http.cookiejar.MozillaCookieJar(COOKIE_FILE)
    session = get_session()
    session.cookies = cookies

    response = session.post(signin_url, credentials, headers=headers)

    logging.info(f"{signin_url} was executed | Status-Code:{response.status_code}")

    if response.status_code == 201:  # NO MFA
        cookies.save()
        logging.info("Sign-in NO MFA OK")
        return FinapiResponse.success(message="Sign-in done")
    elif response.status_code == 202:  # MFA
        otp_relay_token = response.json()["result"]["otp_relay_token"]
        mfa_data = get_credentials_mfa(mfa_code, otp_relay_token)
        headers["Content-Length"] = f"{len(mfa_data)}"
        response = session.post(signin_url, mfa_data, headers=headers)
        if response.status_code == 201:
            cookies.save()
            logging.info("Sign-in MFA OK")
            return FinapiResponse.success(message="Sign-in done")
        else:
            logging.error(f"Sign-in fail MFA KO | ERROR-CODE:{response.status_code}")
            return FinapiResponse.error(
                status_code=response.status_code, message=json.loads(response.text)["error"]["code"]
            )
    else:
        logging.error(f"Sign-in fail | ERROR-CODE: {response.status_code}")
        return FinapiResponse.error(status_code=response.status_code, message=response.reason)
