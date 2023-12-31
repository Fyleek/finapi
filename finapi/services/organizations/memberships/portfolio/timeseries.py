from finapi.schemas import FinaryResponse, Period, TimeseriesType, Categories
from finapi.utils import get_request


def get_timeseries_portfolio(
        organization_id: str,
        membership_id: str,
        period: Period,
        timeseries_type: TimeseriesType,
        categories: Categories
) -> FinaryResponse:
    return get_request(f"organizations/{organization_id}"
                       f"/memberships/{membership_id}"
                       f"/portfolio/timeseries"
                       f"?period={period}"
                       f"&type={timeseries_type}"
                       f"&categories={categories}")