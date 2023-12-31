from enum import Enum
from typing import List
from pydantic import BaseModel


# Default empty (all's)
class Categorie(str, Enum):
    INVESTMENTS = "investments"
    SAVINGS = "savings"
    CHECKINGS = "checkings"


class Categories(BaseModel):
    categories: List[Categorie]


def format_categories(categories: Categories) -> str:
    # Join the categories using '%2C' which is URL encoded for ','
    return '%2C'.join(category.value for category in categories.categories)

# Default value:
# categories: Optional[categories] = ""
