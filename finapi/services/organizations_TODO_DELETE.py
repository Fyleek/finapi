from finapi.schemas import FinaryResponse
from finapi.utils import get_request


# Direct Finary response

def get_organizations_request() -> FinaryResponse:
    return get_request("users/me/organizations")


def get_organization_holdings_accounts(organization_id: str, user_id: str, without_empty: bool) -> FinaryResponse:
    return get_request(
        f"organizations/{organization_id}/memberships/{user_id}/holdings_accounts?without_empty={without_empty}")


# TODO "categories" optional
def get_portfolio(organization_id: str, user_id: str, new_format: bool, period: str, categories: str) -> FinaryResponse:
    return get_request(
        f"organizations/{organization_id}/memberships/{user_id}/portfolio?new_format={new_format}&period={period}&categories={categories}")


def get_portfolio_time_series(organization_id: str, user_id: str, period: str, dashboard_type: str = "gross") -> FinaryResponse:
    return get_request(
        f"organizations/{organization_id}/memberships/{user_id}/portfolio/timeseries?period={period}&type={dashboard_type}")


def get_time_series(organization_id: str, user_id: str, period: str, type1: str, categories: str) -> FinaryResponse:
    return get_request(
        f"organizations/{organization_id}/memberships/{user_id}/timeseries?period={period}&type={type1}&categories={categories}")

# TODO Check all possible values for category
def get_asset_list(organization_id: str, user_id: str, limit: int, period: str, categories: str, order: str) -> FinaryResponse:
    return get_request(
        f"organizations/{organization_id}/memberships/{user_id}/asset_list?limit={limit}&period={period}&categories={categories}&order={order}")


def get_investments(organization_id: str, user_id: str, period: str) -> FinaryResponse:
    return get_request(f"organizations/{organization_id}/memberships/{user_id}/portfolio/investments?period={period}")


def get_investments_by_distribution(organization_id: str, user_id: str, distribution_type: str, period: str) -> FinaryResponse:
    return get_request(
        f"organizations/{organization_id}/memberships/{user_id}/portfolio/investments/distribution?type={distribution_type}&period={period}")


def get_investments_dividends(organization_id: str, user_id: str) -> FinaryResponse:
    return get_request(f"organizations/{organization_id}/memberships/{user_id}/portfolio/investments/dividends")


def get_investments_sector_allocation(organization_id: str, user_id: str) -> FinaryResponse:
    return get_request(f"organizations/{organization_id}/memberships/{user_id}/portfolio/investments/sector_allocation")


def get_investments_geographical_allocation(organization_id: str, user_id: str) -> FinaryResponse:
    return get_request(
        f"organizations/{organization_id}/memberships/{user_id}/portfolio/investments/geographical_allocation")


def get_fees(organization_id: str, user_id: str) -> FinaryResponse:
    return get_request(f"organizations/{organization_id}/memberships/{user_id}/portfolio/investments/fees")


def get_transaction_categories(organization_id: str, user_id: str) -> FinaryResponse:
    return get_request(f"organizations/{organization_id}/memberships/{user_id}/transaction_categories")


def get_transactions_investments(organization_id: str, user_id: str, number_of_page: int,
                                 transaction_per_page: int) -> FinaryResponse:
    return get_request(
        f"organizations/{organization_id}/memberships/{user_id}/portfolio/investments/transactions?page={number_of_page}&per_page={transaction_per_page}")


def get_transactions_checking_accounts(organization_id: str, user_id: str, number_of_page: int,
                                       transaction_per_page: int) -> FinaryResponse:
    return get_request(
        f"organizations/{organization_id}/memberships/{user_id}/portfolio/checking_accounts/transactions?page={number_of_page}&per_page={transaction_per_page}")


def get_accounts_with_transactions(organization_id: str, user_id: str, with_transaction: bool,
                                   asset_category: str) -> FinaryResponse:
    return get_request(
        f"organizations/{organization_id}/memberships/{user_id}/portfolio/investments/accounts?with_transaction{with_transaction}&asset_category={asset_category}")

def get_savings_accounts(organization_id: str, user_id: str, period: str) -> FinaryResponse:
    return get_request(f"organizations/{organization_id}/memberships/{user_id}/portfolio/savings_accounts/accounts?period={period}")

f"organizations/{organization_id}/memberships/{user_id}/portfolio/commodities/accounts?period={period}&categories={categories}"
f"organizations/{organization_id}/memberships/{user_id}/portfolio/credit_accounts/accounts?period={period}&categories={categories}"
f"organizations/{organization_id}/memberships/{user_id}/portfolio/crowndlendings/accounts?period={period}&categories={categories}"
f"organizations/{organization_id}/memberships/{user_id}/portfolio/cryptos/accounts?period={period}&categories={categories}"
f"organizations/{organization_id}/memberships/{user_id}/portfolio/fonds_euro/accounts?period={period}&categories={categories}"
f"organizations/{organization_id}/memberships/{user_id}/portfolio/loans/accounts?period={period}&categories={categories}"
f"organizations/{organization_id}/memberships/{user_id}/portfolio/other_assets/accounts?period={period}&categories={categories}"
f"organizations/{organization_id}/memberships/{user_id}/portfolio/real_estates/accounts?period={period}&categories={categories}"
f"organizations/{organization_id}/memberships/{user_id}/portfolio/savings_accounts/distribution?period={period}&categories={categories}"
f"organizations/{organization_id}/memberships/{user_id}/wealth/fees"
f"organizations/{organization_id}/memberships/{user_id}/portfolio/savings_accounts?period{period}"
f"organizations/{organization_id}/memberships/{user_id}/portfolio/savings_accounts/timeseries?type{type1}&period={period}"
f"organizations/{organization_id}/memberships/{user_id}/portfolio/checking_accounts/timeseries?type={type1}&period={period}"
f"organizations/{organization_id}/memberships/{user_id}/portfolio/sector_diversification"
f"organizations/{organization_id}/memberships/{user_id}/portfolio/geographical_diversification"
#Insights
f"organizations/{organization_id}/memberships/{user_id}/portfolio/assets_leaderboard?type={type}&mode={mode}" # Check different value for type & mode   str / str
f"organizations/{organization_id}/memberships/{user_id}/views/insights"
f"organizations/{organization_id}/memberships/{user_id}/insights/financial_projection?montly_contribution={ammount}&duration={year}" # int / int




# Custom Finary response
# TODO Create all sorts, data selections with Direct Finary response

# TODO create schema + only return organization result
def get_organization_list():
    return get_organizations_request()
