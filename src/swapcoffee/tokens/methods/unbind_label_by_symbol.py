from stollen.enums import HTTPMethod
from stollen.requests.fields import PlaceholderField

from ..types import BlockchainToken
from .base import SwapCoffeeMethod


class UnbindLabelBySymbol(
    SwapCoffeeMethod[BlockchainToken],
    http_method=HTTPMethod.DELETE,
    api_method="/v2/labels/{label_id}/symbol/{symbol}",
    returning=BlockchainToken,
):
    label_id: int = PlaceholderField()
    symbol: str = PlaceholderField()
