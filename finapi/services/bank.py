from finapi.schemas import FinaryResponse
from finapi.utils import get_request

# TODO Create "type" schema = ["invest"|"cash"] => Default "invest"

# TODO Check if another value is possible for type
def get_bank_account_types(type: str) -> FinaryResponse:
    return get_request(f"bank_account_types?type{type}")
