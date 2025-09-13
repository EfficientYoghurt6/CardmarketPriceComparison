"""Utility helpers for configuration and API key management."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Optional

ENV_PATH = Path(__file__).resolve().parent.parent / ".env"


def _load_env() -> None:
    if not ENV_PATH.exists():
        return
    for line in ENV_PATH.read_text().splitlines():
        if not line or line.startswith("#"):
            continue
        key, _, value = line.partition("=")
        os.environ.setdefault(key, value)


_load_env()


def get_cardmarket_key() -> Optional[str]:
    """Return the configured Cardmarket API key if present."""

    return os.getenv("CARDMARKET_API_KEY")


def set_cardmarket_key(key: str) -> None:
    """Persist the Cardmarket API key to the local ``.env`` file."""

    lines: list[str] = []
    if ENV_PATH.exists():
        lines = [
            line
            for line in ENV_PATH.read_text().splitlines()
            if not line.startswith("CARDMARKET_API_KEY=")
        ]
    lines.append(f"CARDMARKET_API_KEY={key}")
    ENV_PATH.write_text("\n".join(lines) + "\n")
    os.environ["CARDMARKET_API_KEY"] = key
