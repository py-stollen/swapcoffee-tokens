from decimal import Decimal
from typing import Optional

from .base import SwapCoffeeObject


class StakingPool(SwapCoffeeObject):
    id: int
    address: str
    name: str
    image_url: str
    unstake_url: Optional[str] = None
    exchange_rate: Decimal
    cycle_end: Optional[int] = None
