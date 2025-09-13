import asyncio

import httpx

from app.services.cardmarket import CardmarketClient

def test_get_expansions() -> None:
    async def handler(request: httpx.Request) -> httpx.Response:  # pragma: no cover - executed in test
        return httpx.Response(200, json=[{"set_name": "Test Set"}])

    transport = httpx.MockTransport(handler)

    async def run() -> list[str]:
        async with httpx.AsyncClient(transport=transport) as client:
            cm_client = CardmarketClient(client=client)
            return await cm_client.get_expansions()

    expansions = asyncio.run(run())
    assert expansions == ["Test Set"]


def test_get_cards() -> None:
    async def handler(request: httpx.Request) -> httpx.Response:  # pragma: no cover - executed in test
        assert request.url.params.get("set") == "Test Set"
        data = {
            "data": [
                {"name": "Card A", "card_prices": [{"cardmarket_price": "1.5"}]},
                {"name": "Card B", "card_prices": [{"cardmarket_price": "0"}]},
            ]
        }
        return httpx.Response(200, json=data)

    transport = httpx.MockTransport(handler)

    async def run() -> list[dict[str, float]]:
        async with httpx.AsyncClient(transport=transport) as client:
            cm_client = CardmarketClient(client=client)
            return await cm_client.get_cards("Test Set")

    cards = asyncio.run(run())

    assert cards == [
        {"name": "Card A", "price": 1.5},
        {"name": "Card B", "price": 0.0},
    ]
