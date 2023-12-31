from enum import Enum

# Default sum
class Order(str, Enum):
    HIGH_LOW = "perf_high_low"
    LOW_HIGH = "perf_low_high"
    PERCENT_HIGH_LOW = "perf_percent_high_low"
    PERCENT_LOW_HIGH = "perf_percent_low_high"

# Default value:
# order: Optional[Order] = Query(Order.HIGH_LOW)
