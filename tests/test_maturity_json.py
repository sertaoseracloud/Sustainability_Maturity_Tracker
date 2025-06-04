import json
from pathlib import Path

def test_maturity_json_valid():
    json_path = Path(__file__).resolve().parent.parent / "maturity.json"
    with open(json_path, "r", encoding="utf-8") as f:
        json.load(f)
