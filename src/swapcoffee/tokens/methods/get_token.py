from stollen.enums import HTTPMethod
from stollen.requests.fields import PlaceholderField

from ..types import BlockchainToken
from .base import SwapCoffeeMethod


class GetToken(
    SwapCoffeeMethod[BlockchainToken],
    http_method=HTTPMethod.GET,
    api_method="/v2/tokens/{token_id}",
    returning=BlockchainToken,
):
    token_id: int = PlaceholderField()
