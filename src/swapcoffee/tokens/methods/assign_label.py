from stollen.enums import HTTPMethod
from stollen.requests.fields import PlaceholderField

from ..types import BlockchainToken
from .base import SwapCoffeeMethod


class AssignLabel(
    SwapCoffeeMethod[BlockchainToken],
    http_method=HTTPMethod.PUT,
    api_method="/v2/labels/{label_id}/{token_id}",
    returning=BlockchainToken,
):
    label_id: int = PlaceholderField()
    token_id: int = PlaceholderField()
