"""HTTP client for retrieving expansion and card data.

The real Cardmarket API requires authentication. For the initial
implementation the client consumes the public YGOProDeck API which exposes
similar endpoints for sets and card information.  This allows the backend to
provide useful data without credentials while keeping the service layer
compatible with a future Cardmarket integration.
"""

from typing import Any, Dict, List, Optional

import httpx


class YGOProClient:
    """Client wrapper around the public YGOProDeck API."""

    BASE_URL = "https://db.ygoprodeck.com/api/v7"

    def __init__(self, client: Optional[httpx.AsyncClient] = None) -> None:
        self._client = client

    async def get_expansions(self) -> List[str]:
        """Return available expansion names.

        Uses a provided ``httpx.AsyncClient`` if supplied, otherwise creates a
        temporary client for the request.
        """

        if self._client:
            response = await self._client.get(f"{self.BASE_URL}/cardsets.php")
        else:  # pragma: no cover - simple network call
            async with httpx.AsyncClient() as client:
                response = await client.get(f"{self.BASE_URL}/cardsets.php")

        response.raise_for_status()
        data: List[Dict[str, Any]] = response.json()
        return [entry["set_name"] for entry in data]

    async def get_cards(self, expansion_name: str) -> List[str]:
        """Return card names for a given expansion."""

        if self._client:
            response = await self._client.get(
                f"{self.BASE_URL}/cardinfo.php", params={"set": expansion_name}
            )
        else:  # pragma: no cover - simple network call
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{self.BASE_URL}/cardinfo.php", params={"set": expansion_name}
                )

        response.raise_for_status()
        payload: Dict[str, Any] = response.json()
        return [card["name"] for card in payload.get("data", [])]
