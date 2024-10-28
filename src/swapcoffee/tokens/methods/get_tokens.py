from typing import Optional

from pydantic import Field
from stollen.enums import HTTPMethod

from ..types import BlockchainToken, Page
from .base import SwapCoffeeMethod


class GetTokens(
    SwapCoffeeMethod[Page[BlockchainToken]],
    http_method=HTTPMethod.GET,
    api_method="/v2/tokens",
    returning=Page[BlockchainToken],
):
    search: Optional[str] = None
    blockchain_id: Optional[int] = None
    label_id: Optional[int] = None
    page: Optional[int] = Field(default=None, ge=1)
    size: Optional[int] = Field(default=None, ge=1, le=100)
