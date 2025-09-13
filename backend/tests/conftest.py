import sys
from pathlib import Path

# Ensure the application package is importable during tests
sys.path.append(str(Path(__file__).resolve().parents[1]))
