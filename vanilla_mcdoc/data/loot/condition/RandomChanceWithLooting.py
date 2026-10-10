"""
Generated from symbols.json for ::java::data::loot::condition::RandomChanceWithLooting
Local link to file: vanilla_mcdoc/data/loot/condition/RandomChanceWithLooting.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class RandomChanceWithLooting(GeneratedModel):
    chance: Annotated[float, Field(ge=0, le=1)]
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
