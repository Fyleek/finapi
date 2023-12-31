from enum import Enum

# Default sum
class TimeseriesType(str, Enum):
    ALL = "all"
    SUM = "sum"

# Default value:
# period: Optional[Period] = Query(Period.SUM)
