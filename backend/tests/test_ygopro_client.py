import asyncio

import httpx

from app.services.ygopro import YGOProClient

def test_get_expansions() -> None:
    async def handler(request: httpx.Request) -> httpx.Response:  # pragma: no cover - executed in test
        return httpx.Response(200, json=[{"set_name": "Test Set"}])

    transport = httpx.MockTransport(handler)

    async def run() -> list[str]:
        async with httpx.AsyncClient(transport=transport) as client:
            yg_client = YGOProClient(client=client)
            return await yg_client.get_expansions()

    expansions = asyncio.run(run())
    assert expansions == ["Test Set"]


def test_get_cards() -> None:
    async def handler(request: httpx.Request) -> httpx.Response:  # pragma: no cover - executed in test
        assert request.url.params.get("set") == "Test Set"
        data = {"data": [{"name": "Card A"}, {"name": "Card B"}]}
        return httpx.Response(200, json=data)

    transport = httpx.MockTransport(handler)

    async def run() -> list[str]:
        async with httpx.AsyncClient(transport=transport) as client:
            yg_client = YGOProClient(client=client)
            return await yg_client.get_cards("Test Set")

    cards = asyncio.run(run())

    assert cards == ["Card A", "Card B"]
