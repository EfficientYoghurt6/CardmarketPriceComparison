import asyncio

import httpx

from app.services.cardmarket import CardmarketClient


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
