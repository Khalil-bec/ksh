import json
import os

ALIASES_FILE = os.path.expanduser("~/.ksh_aliases")

def charger_aliases():
    if not os.path.exists(ALIASES_FILE):
        return {}
    with open(ALIASES_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def sauvegarder_aliases(aliases):
    with open(ALIASES_FILE, "w") as f:
        json.dump(aliases, f, indent=2)

ALIASES = charger_aliases()