import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def load_metadata():

    metadata_path = (
        PROJECT_ROOT /
        "models" /
        "deployment" /
        "metadata.json"
    )

    with open(metadata_path) as f:
        return json.load(f)