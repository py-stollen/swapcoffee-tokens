from stollen.enums import HTTPMethod
from stollen.requests.fields import PlaceholderField

from ..types import BlockchainToken
from .base import SwapCoffeeMethod


class GetTokenBySymbol(
    SwapCoffeeMethod[BlockchainToken],
    http_method=HTTPMethod.GET,
    api_method="/v2/tokens/symbol/{symbol}",
    returning=BlockchainToken,
):
    symbol: str = PlaceholderField()
