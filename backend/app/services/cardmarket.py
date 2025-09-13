"""Client for retrieving card prices from the Cardmarket API."""

from __future__ import annotations

from typing import Optional

import httpx

from ..config import get_cardmarket_key


class CardmarketClient:
    """Minimal async client for Cardmarket pricing."""

    BASE_URL = "https://api.cardmarket.com/ws/v2.0/output.json"

    def __init__(
        self,
        api_key: Optional[str] = None,
        client: Optional[httpx.AsyncClient] = None,
    ) -> None:
        self._api_key = api_key or get_cardmarket_key()
        self._client = client

    async def get_price(self, product_name: str) -> float:
        """Return the market price for ``product_name``.

        If no API key is configured the function returns ``0.0``.
        """

        if not self._api_key:
            return 0.0

        headers = {"Authorization": f"Bearer {self._api_key}"}
        url = f"{self.BASE_URL}/products/{product_name}"

        if self._client:
            response = await self._client.get(url, headers=headers)
        else:  # pragma: no cover - simple network call
            async with httpx.AsyncClient() as client:
                response = await client.get(url, headers=headers)

        response.raise_for_status()
        data = response.json()
        return float(data.get("price", 0.0))
