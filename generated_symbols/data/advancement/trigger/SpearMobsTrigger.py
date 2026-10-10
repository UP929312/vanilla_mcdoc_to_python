"""
Generated from symbols.json for ::java::data::advancement::trigger::SpearMobsTrigger
Local link to file: generated_symbols/data/advancement/trigger/SpearMobsTrigger.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from generated_symbols.data.advancement.trigger.AllOptional import AllOptional
from generated_symbols.data.advancement.trigger.PlayerConditions import PlayerConditions


class SpearMobsTriggerTypeArg(PlayerConditions):
    count: Annotated[int, Field(ge=1)] | None = None  # Minimum mob count required.


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

