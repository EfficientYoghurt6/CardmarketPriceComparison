from typing import Dict, List

from fastapi import APIRouter
from pydantic import BaseModel

from ..services.cardmarket import CardmarketClient
from ..services.ev import calculate_ev


router = APIRouter()

cardmarket_client = CardmarketClient()


@router.get("/expansions")
async def list_expansions() -> Dict[str, List[str]]:
    """Return available Yugioh expansions."""

    expansions = await cardmarket_client.get_expansions()
    return {"expansions": expansions}


@router.get("/expansions/{expansion_name}/cards")
async def list_cards(expansion_name: str) -> Dict[str, List[Dict[str, float]]]:
    """Return card data for the requested expansion."""

    cards = await cardmarket_client.get_cards(expansion_name)
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
