from stollen import StollenMethod
from stollen.types import StollenT

from ..client import SwapCoffee


class SwapCoffeeMethod(
    StollenMethod[StollenT, SwapCoffee],
    abstract=True,
):
    pass
