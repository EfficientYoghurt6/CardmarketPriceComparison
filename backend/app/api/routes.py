from typing import Dict, List

from fastapi import APIRouter
from pydantic import BaseModel

from ..config import get_cardmarket_key, set_cardmarket_key
from ..services.cardmarket import CardmarketClient
from ..services.ev import calculate_ev
from ..services.ygopro import YGOProClient


router = APIRouter()

ygopro_client = YGOProClient()
cardmarket_client = CardmarketClient()


@router.get("/expansions")
async def list_expansions() -> Dict[str, List[str]]:
    """Return available Yugioh expansions."""

    expansions = await ygopro_client.get_expansions()
    return {"expansions": expansions}


@router.get("/expansions/{expansion_name}/cards")
async def list_cards(expansion_name: str) -> Dict[str, List[Dict[str, float]]]:
    """Return card data for the requested expansion."""

    names = await ygopro_client.get_cards(expansion_name)
    cards: List[Dict[str, float]] = []
    for name in names:
        price = await cardmarket_client.get_price(name)
        cards.append({"name": name, "price": price})
    return {"expansion": expansion_name, "cards": cards}


class CardPrice(BaseModel):
    name: str
    price: float


class EVRequest(BaseModel):
    cards: List[CardPrice]
    probabilities: Dict[str, float]


@router.post("/ev")
async def calculate_ev_endpoint(ev_request: EVRequest) -> Dict[str, float]:
    """Calculate expected value from card prices and probabilities."""

    cards_payload = [card.dict() for card in ev_request.cards]
    ev = calculate_ev(cards_payload, ev_request.probabilities)
    return {"ev": ev}


class APIKeyPayload(BaseModel):
    api_key: str


@router.post("/apikey")
async def set_api_key(payload: APIKeyPayload) -> Dict[str, str]:
    """Store the Cardmarket API key on the server."""

    set_cardmarket_key(payload.api_key)
    return {"status": "stored"}


@router.get("/apikey")
async def get_api_key() -> Dict[str, bool]:
    """Return whether a Cardmarket API key has been configured."""

    return {"configured": get_cardmarket_key() is not None}
