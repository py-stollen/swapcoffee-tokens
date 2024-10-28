from typing import Optional

from pydantic import Field
from stollen.enums import HTTPMethod

from ..types import Page, TokenLabel
from .base import SwapCoffeeMethod


class GetLabels(
    SwapCoffeeMethod[Page[TokenLabel]],
    http_method=HTTPMethod.GET,
    api_method="/v2/labels",
    returning=Page[TokenLabel],
):
    page: Optional[int] = Field(default=None, ge=1)
    size: Optional[int] = Field(default=None, ge=1, le=100)
