from finapi.utils import get_header_login


def test_get_header_login():
    content = '{"user":"test","password":"test123"}'

    headers = get_header_login(content)

    expected_content_length = str(len(content))

    assert headers["Content-Length"] == expected_content_length
    assert headers["Content-Type"] == "application/json; charset=utf-8"
