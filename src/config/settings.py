import json
import os

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "defaults.json")

with open(CONFIG_PATH) as f:
    CONFIG = json.load(f)

DEFAULT_REGION = CONFIG.get("default_region", "us-east-1")
