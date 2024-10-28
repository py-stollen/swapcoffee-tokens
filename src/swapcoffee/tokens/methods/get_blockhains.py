from stollen.enums import HTTPMethod

from ..types import Blockchain
from .base import SwapCoffeeMethod


class GetBlockchains(
    SwapCoffeeMethod[list[Blockchain]],
    http_method=HTTPMethod.GET,
    api_method="/api/v2/tokens/blockchains",
    returning=list[Blockchain],
):
    pass
