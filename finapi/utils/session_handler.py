import requests
import http.cookiejar

from finapi.constants import COOKIE_FILE


def get_session() -> requests.Session:
    session = requests.Session()
    cookies = http.cookiejar.MozillaCookieJar(COOKIE_FILE)
    cookies.load()
    session.cookies = cookies
    return session
