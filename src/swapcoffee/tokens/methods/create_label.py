from stollen.enums import HTTPMethod

from ..types import TokenLabel
from .base import SwapCoffeeMethod


class CreateLabel(
    SwapCoffeeMethod[TokenLabel],
    http_method=HTTPMethod.POST,
    api_method="/v2/labels",
    returning=TokenLabel,
):
    name: str
    color: str
