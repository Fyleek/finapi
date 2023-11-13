import requests
import http.cookiejar


def get_session(cookies: http.cookiejar.MozillaCookieJar) -> requests.Session:
    session = requests.Session()
    session.cookies = cookies
    return session
