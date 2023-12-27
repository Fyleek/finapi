from finapi.schemas import FinaryResponse
from finapi.utils import get_request

from organizations_service import get_organization_list


# Direct Finary response
def get_me_request() -> FinaryResponse:
    return get_request("users/me")


def get_subscription_details() -> FinaryResponse:
    return get_request("users/me/subscription_details")


# Custom Finary response
# TODO Create all sorts, data selections with Direct Finary response

# TODO create schema + return all users per organization
def get_users_per_organization():
    organizations = get_organization_list()
