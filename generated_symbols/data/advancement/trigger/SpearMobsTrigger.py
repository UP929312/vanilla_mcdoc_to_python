"""
Generated from symbols.json for ::java::data::advancement::trigger::SpearMobsTrigger
Local link to file: generated_symbols/data/advancement/trigger/SpearMobsTrigger.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated

from generated_symbols.data.advancement.trigger.AllOptional import AllOptional
from generated_symbols.data.advancement.trigger.PlayerConditions import PlayerConditions


@dataclass(kw_only=True)
class SpearMobsTriggerTypeArg(PlayerConditions):
    count: Annotated[int, 'Range | `1` and above | inclusive'] | None = None  # Minimum mob count required.


SpearMobsTrigger = AllOptional[SpearMobsTriggerTypeArg]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::SpearMobsTrigger": {
        "kind": "concrete",
        "child": {
            "kind": "reference",
            "path": "::java::data::advancement::trigger::AllOptional"
        },
        "typeArgs": [
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "spread",
                        "type": {
                            "kind": "reference",
                            "path": "::java::data::advancement::trigger::PlayerConditions"
                        }
                    },
                    {
                        "kind": "pair",
                        "desc": "Minimum mob count required.",
                        "key": "count",
                        "type": {
                            "kind": "int",
                            "valueRange": {
                                "kind": 0,
                                "min": 1
                            }
                        },
                        "optional": True
                    }
                ]
            }
        ]
    }
}

