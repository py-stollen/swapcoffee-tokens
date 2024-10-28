from stollen.enums import HTTPMethod
from stollen.requests.fields import PlaceholderField

from ..types import TokenLabel
from .base import SwapCoffeeMethod


class UpdateLabel(
    SwapCoffeeMethod[TokenLabel],
    http_method=HTTPMethod.PUT,
    api_method="/v2/labels/{label_id}",
    returning=TokenLabel,
):
    label_id: int = PlaceholderField()
    color: str
