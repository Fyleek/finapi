def get_header_login(content: str) -> dict[str, str]:
    headers = {
        "Content-Length": f"{len(content)}",
        "Content-Type": "application/json; charset=utf-8",
    }
    return headers
