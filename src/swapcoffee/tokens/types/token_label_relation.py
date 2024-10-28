from datetime import datetime
from typing import Optional

from .base import SwapCoffeeObject


class TokenLabelRelation(SwapCoffeeObject):
    token_id: int
    label_id: int
    expires_at: Optional[datetime] = None
