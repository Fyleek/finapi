from enum import Enum


# Default gross
class DashboardType(str, Enum):
    GROSS = "gross"
    NET = "net"
    FINARY = "finary"

# Default value:
# dashboard_type: Optional[DashboardType] = Query(DashboardType.GROSS)
