# Generated from symbols.json for ::java::data::loot::condition::RandomChanceWithLooting
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class RandomChanceWithLooting:
    chance: Annotated[float, 'Range | `0`-`1` | both inclusive']
    looting_multiplier: float  # Looting adjustment to the base success rate. Formula is `chance + (looting_level * looting_multiplier)` .


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::condition::RandomChanceWithLooting": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "chance",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1
                    }
                }
            },
            {
                "kind": "pair",
                "desc": "Looting adjustment to the base success rate. Formula is `chance + (looting_level * looting_multiplier)` .",
                "key": "looting_multiplier",
                "type": {
                    "kind": "float"
                }
            }
        ]
    }
}

