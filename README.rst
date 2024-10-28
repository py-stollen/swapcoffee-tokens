
#################
swapcoffee-tokens
#################

Installation
------------

..  code-block:: bash

    pip install -U swapcoffee-tokens

Simple example
--------------

.. code-block:: python

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

Donations
---------
TON: `UQAYJ1terNmvoBh26Xi7tLa_P4t_OGMZOXBUfDB2mLMGuVMb`
USDT TRC20: `TGr2J3Pi6WmcexwmGFJDHLqrrhDoe2U6w6`
