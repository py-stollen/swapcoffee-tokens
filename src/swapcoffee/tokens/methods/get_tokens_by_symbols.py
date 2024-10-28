from pydantic import RootModel
from stollen.enums import HTTPMethod

from ..types import BlockchainToken
from .base import SwapCoffeeMethod


class GetTokensBySymbols(
    SwapCoffeeMethod[list[BlockchainToken]],
    RootModel[list[str]],
    http_method=HTTPMethod.POST,
    api_method="/v2/tokens/by-symbols",
    returning=list[BlockchainToken],
):
    pass
