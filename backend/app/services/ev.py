"""Utility for expected value calculations."""

from math import isclose
from typing import Dict, Iterable


def calculate_ev(cards: Iterable[dict], probabilities: Dict[str, float]) -> float:
    """Compute the expected value of drawing a card.

    Parameters
    ----------
    cards:
        Iterable of card dictionaries containing at least ``name`` and ``price``.
    probabilities:
        Mapping of card names to the probability of pulling that card.

    Returns
    -------
    float
        The expected monetary value of one draw.

    Raises
    ------
    ValueError
        If the provided probabilities do not sum to 1.
    """

    total_prob = sum(probabilities.values())
    if not isclose(total_prob, 1.0, rel_tol=1e-9):
        raise ValueError("Probabilities must sum to 1")

    ev = 0.0
    for card in cards:
        price = float(card.get("price", 0.0))
        ev += price * probabilities.get(card.get("name"), 0.0)
    return ev
