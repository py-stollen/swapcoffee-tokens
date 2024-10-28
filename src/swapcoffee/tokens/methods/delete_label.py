from stollen.enums import HTTPMethod
from stollen.requests.fields import PlaceholderField

from ..types import Message
from .base import SwapCoffeeMethod


class DeleteLabel(
    SwapCoffeeMethod[Message],
    http_method=HTTPMethod.DELETE,
    api_method="/v2/labels/{label_id}",
    returning=Message,
):
    label_id: int = PlaceholderField()
