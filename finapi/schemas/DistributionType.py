from enum import Enum


# Default "type"
class DistributionType(str, Enum):
    STOCK = "stock"
    ACCOUNT = "account"
    TYPE = "type"
