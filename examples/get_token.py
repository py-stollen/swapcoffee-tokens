import asyncio
import logging

from swapcoffee.tokens import SwapCoffee
from swapcoffee.tokens.types import BlockchainToken


async def main() -> None:
    logging.basicConfig(level=logging.DEBUG)
    coffee: SwapCoffee = SwapCoffee()
    tokens: list[BlockchainToken] = await coffee.get_tokens_by_symbols(symbols=["NOT", "DMT"])
    for token in tokens:
        logging.info("Token %s ($%s) costs %s USD", token.name, token.symbol, token.price_usd)
    await coffee.session.close()


if __name__ == "__main__":
    asyncio.run(main())
