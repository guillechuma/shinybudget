from dataclasses import dataclass
from datetime import date

@dataclass
class Expense:
    id: int
    date: date
    amount: float
    description: str
    category_id: int