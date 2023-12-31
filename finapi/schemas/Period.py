from enum import Enum


# Default all
class Period(str, Enum):
    ONE_MONTH = "1m"
    ONE_WEEK = "1w"
    ONE_DAY = "1d"
    ONE_YEAR = "1y"
    ALL = "all"
    FINARY = "ytd"

# Default value:
# period: Optional[Period] = Query(Period.ALL)
