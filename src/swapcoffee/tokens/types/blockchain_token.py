from decimal import Decimal
from typing import Optional

from .base import SwapCoffeeObject
from .staking_pool import StakingPool
from .token_label_relation import (
    TokenLabelRelation,
)


class BlockchainToken(SwapCoffeeObject):
    id: int
    blockchain_id: int
    address: str
    name: str
    symbol: str
    decimals: int
    price_usd: Optional[Decimal] = None
    price_change_24h: Optional[Decimal] = None
    tvl: Optional[Decimal] = None
    holders_count: Optional[int] = None
    image: Optional[str] = None
    external_id: Optional[str] = None
    trust_score: Optional[float] = None
    stacking_pool_id: Optional[int] = None
    staking_pool: Optional[StakingPool] = None
    labels: Optional[list[TokenLabelRelation]] = None
