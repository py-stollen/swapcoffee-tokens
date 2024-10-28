from typing import Optional

from .base import SwapCoffeeObject


class Blockchain(SwapCoffeeObject):
    id: Optional[int] = None
    name: str
