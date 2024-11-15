from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

from stollen import Stollen
from stollen.requests.fields import Header

from .exceptions import (
    ForbiddenError,
    InternalServerError,
    RateLimitError,
    SwapCoffeeAPIError,
    ValidationError,
    NotFoundError,
)

if TYPE_CHECKING:
    from .types import (
        Blockchain,
        BlockchainToken,
        Message,
        Page,
        TokenLabel,
    )


class SwapCoffee(Stollen):
    def __init__(
        self,
        http_bearer: Optional[str] = None,
        **stollen_kwargs: Any,
    ) -> None:
        if http_bearer:
            fields = stollen_kwargs.setdefault("global_request_fields", [])
            fields.append(Header(name="HTTPBearer", value=http_bearer))
        super().__init__(
            base_url="https://tokens.swap.coffee/api",
            general_error_class=SwapCoffeeAPIError,
            error_codes={
                403: ForbiddenError,
                404: NotFoundError,
                422: ValidationError,
                429: RateLimitError,
                500: InternalServerError,
            },
            error_message_key=["detail"],
            **stollen_kwargs,
        )

    async def assign_label(self, label_id: int, token_id: int) -> BlockchainToken:
        from .methods import AssignLabel

        call: AssignLabel = AssignLabel(label_id=label_id, token_id=token_id)

        return await self(call)

    async def assign_label_by_address(self, label_id: int, address: str) -> BlockchainToken:
        from .methods import AssignLabelByAddress

        call: AssignLabelByAddress = AssignLabelByAddress(label_id=label_id, address=address)

        return await self(call)

    async def assign_label_by_symbol(self, label_id: int, symbol: str) -> BlockchainToken:
        from .methods import AssignLabelBySymbol

        call: AssignLabelBySymbol = AssignLabelBySymbol(label_id=label_id, symbol=symbol)

        return await self(call)

    async def create_label(self, name: str, color: str) -> TokenLabel:
        from .methods import CreateLabel

        call: CreateLabel = CreateLabel(name=name, color=color)

        return await self(call)

    async def delete_label(self, label_id: int) -> Message:
        from .methods import DeleteLabel

        call: DeleteLabel = DeleteLabel(label_id=label_id)

        return await self(call)

    async def get_blockchains(
        self,
    ) -> list[Blockchain]:
        from .methods import GetBlockchains

        call: GetBlockchains = GetBlockchains()

        return await self(call)

    async def get_labels(
        self,
        page: Optional[int] = None,
        size: Optional[int] = None,
    ) -> Page[TokenLabel]:
        from .methods import GetLabels

        call: GetLabels = GetLabels(page=page, size=size)

        return await self(call)

    async def get_token(self, token_id: int) -> BlockchainToken:
        from .methods import GetToken

        call: GetToken = GetToken(token_id=token_id)

        return await self(call)

    async def get_token_by_address(self, address: str) -> BlockchainToken:
        from .methods import GetTokenByAddress

        call: GetTokenByAddress = GetTokenByAddress(address=address)

        return await self(call)

    async def get_token_by_symbol(self, symbol: str) -> BlockchainToken:
        from .methods import GetTokenBySymbol

        call: GetTokenBySymbol = GetTokenBySymbol(symbol=symbol)

        return await self(call)

    async def get_tokens(
        self,
        search: Optional[str] = None,
        blockchain_id: Optional[int] = None,
        label_id: Optional[int] = None,
        page: Optional[int] = None,
        size: Optional[int] = None,
    ) -> Page[BlockchainToken]:
        from .methods import GetTokens

        call: GetTokens = GetTokens(
            search=search,
            blockchain_id=blockchain_id,
            label_id=label_id,
            page=page,
            size=size,
        )

        return await self(call)

    async def get_tokens_by_addresses(self, addresses: list[str]) -> list[BlockchainToken]:
        from .methods import GetTokensByAddresses

        call: GetTokensByAddresses = GetTokensByAddresses(addresses)

        return await self(call)

    async def get_tokens_by_symbols(self, symbols: list[str]) -> list[BlockchainToken]:
        from .methods import GetTokensBySymbols

        call: GetTokensBySymbols = GetTokensBySymbols(symbols)

        return await self(call)

    async def unbind_label(self, label_id: int, token_id: int) -> BlockchainToken:
        from .methods import UnbindLabel

        call: UnbindLabel = UnbindLabel(label_id=label_id, token_id=token_id)

        return await self(call)

    async def unbind_label_by_symbol(self, label_id: int, symbol: str) -> BlockchainToken:
        from .methods import UnbindLabelBySymbol

        call: UnbindLabelBySymbol = UnbindLabelBySymbol(label_id=label_id, symbol=symbol)

        return await self(call)

    async def update_label(self, label_id: int, color: str) -> TokenLabel:
        from .methods import UpdateLabel

        call: UpdateLabel = UpdateLabel(label_id=label_id, color=color)

        return await self(call)
