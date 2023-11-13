import http.cookiejar

from finapi.utils import get_session


def test_get_session():
    mock_cookiejar = http.cookiejar.MozillaCookieJar()

    cookie = http.cookiejar.Cookie(
        version=0,
        name="test",
        value="value",
        port=None,
        port_specified=False,
        domain="www.example.com",
        domain_specified=False,
        domain_initial_dot=False,
        path="/",
        path_specified=True,
        secure=False,
        expires=None,
        discard=True,
        comment=None,
        comment_url=None,
        rest={"HttpOnly": "true"},
        rfc2109=False,
    )
    mock_cookiejar.set_cookie(cookie)

    session = get_session(mock_cookiejar)

    assert any(c.name == "test" and c.value == "value" for c in session.cookies)
