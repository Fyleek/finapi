from finapi.schemas import FinaryResponse
from finapi.utils import get_request


def get_subscription_details_request() -> FinaryResponse:
    return get_request("users/me/subscription_details")
