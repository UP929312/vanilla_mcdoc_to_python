"""
Generated from symbols.json for ::java::data::advancement::trigger::UsedEnderEyeTrigger
Local link to file: generated_symbols/data/advancement/trigger/UsedEnderEyeTrigger.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass

from generated_symbols.data.advancement.trigger.AllOptional import AllOptional
from generated_symbols.data.advancement.trigger.PlayerConditions import PlayerConditions
from generated_symbols.data.util.MinMaxBounds import MinMaxBounds


@dataclass(kw_only=True)
class UsedEnderEyeTriggerTypeArg(PlayerConditions):
    distance: MinMaxBounds[float] | float | None = None  # Horizontal distance between the player and the stronghold.


UsedEnderEyeTrigger = AllOptional[UsedEnderEyeTriggerTypeArg]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::UsedEnderEyeTrigger": {
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
                        "desc": "Horizontal distance between the player and the stronghold.",
                        "key": "distance",
                        "type": {
                            "kind": "concrete",
                            "child": {
                                "kind": "reference",
                                "path": "::java::data::util::MinMaxBounds"
                            },
                            "typeArgs": [
                                {
                                    "kind": "double"
                                }
                            ]
                        },
                        "optional": True
                    }
                ]
            }
        ]
    }
}

