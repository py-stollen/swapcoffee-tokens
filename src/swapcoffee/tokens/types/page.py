from typing import Any, Generic, Optional, TypeVar

from .base import SwapCoffeeObject

T = TypeVar("T", bound=Any)


class Page(SwapCoffeeObject, Generic[T]):
    items: list[T]
    total: int
    page: int
    size: int
    pages: Optional[int] = None
