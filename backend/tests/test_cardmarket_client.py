import asyncio

import httpx

from app.services.cardmarket import CardmarketClient
from app.services.ygopro import YGOProClient


def test_get_price_includes_auth_header() -> None:
    async def handler(request: httpx.Request) -> httpx.Response:  # pragma: no cover - executed in test
        assert request.headers.get("Authorization") == "Bearer test-key"
        return httpx.Response(200, json={"price": 2.5})

    transport = httpx.MockTransport(handler)

    async def run() -> float:
        async with httpx.AsyncClient(transport=transport) as client:
            cm_client = CardmarketClient(api_key="test-key", client=client)
            return await cm_client.get_price("Blue-Eyes")

    price = asyncio.run(run())
    assert price == 2.5


def test_get_price_without_key_uses_ygopro() -> None:
    async def handler(request: httpx.Request) -> httpx.Response:  # pragma: no cover - executed in test
        assert request.url.params.get("name") == "Dark Magician"
        data = {"data": [{"card_prices": [{"cardmarket_price": "0.45"}]}]}
        return httpx.Response(200, json=data)

    transport = httpx.MockTransport(handler)

    async def run() -> float:
        async with httpx.AsyncClient(transport=transport) as client:
            yg_client = YGOProClient(client=client)
            cm_client = CardmarketClient(ygopro_client=yg_client)
            return await cm_client.get_price("Dark Magician")

    price = asyncio.run(run())
    assert price == 0.45
