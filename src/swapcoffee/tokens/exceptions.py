from typing import Any

from stollen.exceptions import StollenAPIError
from stollen.requests.types import (
    StollenRequest,
    StollenResponse
)


def resolve_error_message(message: str, response: StollenResponse) -> str:
    if response.status_code == 403 and message == "Not authenticated":
        return "You are not authenticated to use this method. Please provide a valid token."
    return f"CoffeeSwap says: {message}"


class SwapCoffeeAPIError(StollenAPIError):
    def __init__(
        self,
        message: str,
        request: StollenRequest,
        response: StollenResponse,
        **kwargs: Any,
    ) -> None:
        super().__init__(
            message=resolve_error_message(message, response),
            request=request,
            response=response,
            **kwargs,
        )


class ForbiddenError(SwapCoffeeAPIError):
    pass


class NotFoundError(SwapCoffeeAPIError):
    pass


class ValidationError(SwapCoffeeAPIError):
    pass


class RateLimitError(SwapCoffeeAPIError):
    pass


class InternalServerError(SwapCoffeeAPIError):
    pass
