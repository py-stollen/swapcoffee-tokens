from stollen.enums import HTTPMethod
from stollen.requests.fields import PlaceholderField

from ..types import BlockchainToken
from .base import SwapCoffeeMethod


class GetTokenByAddress(
    SwapCoffeeMethod[BlockchainToken],
    http_method=HTTPMethod.GET,
    api_method="/v2/tokens/address/{address}",
    returning=BlockchainToken,
):
    address: str = PlaceholderField()
