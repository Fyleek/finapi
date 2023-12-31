from finapi.schemas import FinaryResponse
from finapi.utils import get_request


def get_asset_list_for(organization_id: str, membership_id: str) -> FinaryResponse:
    return get_request(f"/organizations/{organization_id}/memberships/{membership_id}/asset_list")


def get_asset_list_categories(organization_id: str, membership_id: str) -> FinaryResponse:
    return get_request(f"/organizations/{organization_id}/memberships/{membership_id}/asset_list/categories")
