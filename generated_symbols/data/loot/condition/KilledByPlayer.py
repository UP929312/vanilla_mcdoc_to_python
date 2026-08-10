"""
Generated from symbols.json for ::java::data::loot::condition::KilledByPlayer
Local link to file: generated_symbols/data/loot/condition/KilledByPlayer.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass


@dataclass(kw_only=True)
class KilledByPlayer:
    inverse: bool | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::condition::KilledByPlayer": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "inverse",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

