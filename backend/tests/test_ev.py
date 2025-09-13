import pytest

from app.services.ev import calculate_ev


def test_calculate_ev() -> None:
    cards = [{"name": "A", "price": 1.0}, {"name": "B", "price": 2.0}]
    probabilities = {"A": 0.25, "B": 0.75}
    assert calculate_ev(cards, probabilities) == pytest.approx(1.75)


def test_calculate_ev_invalid_probabilities() -> None:
    cards = [{"name": "A", "price": 1.0}]
    probabilities = {"A": 0.2}
    with pytest.raises(ValueError):
        calculate_ev(cards, probabilities)
