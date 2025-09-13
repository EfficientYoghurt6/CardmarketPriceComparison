"""Console helpers for managing API keys."""

from __future__ import annotations

import argparse
import getpass

from .config import set_cardmarket_key


def main() -> None:
    parser = argparse.ArgumentParser(description="Configure API keys")
    parser.add_argument("--key", help="Cardmarket API key")
    args = parser.parse_args()

    key = args.key or getpass.getpass("Cardmarket API key: ")
    set_cardmarket_key(key)
    print("Cardmarket API key stored.")


if __name__ == "__main__":
    main()
