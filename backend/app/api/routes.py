from fastapi import APIRouter

router = APIRouter()

@router.get("/expansions")
async def list_expansions() -> dict:
    """Placeholder endpoint returning available Yugioh expansions."""
    return {"expansions": []}

@router.get("/expansions/{expansion_id}/cards")
async def list_cards(expansion_id: int) -> dict:
    """Placeholder endpoint returning cards for an expansion."""
    return {"expansion_id": expansion_id, "cards": []}

@router.post("/ev")
async def calculate_ev(ev_request: dict) -> dict:
    """Placeholder endpoint for EV calculation."""
    return {"ev": 0}
