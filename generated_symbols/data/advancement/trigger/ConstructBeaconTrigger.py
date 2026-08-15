"""
Generated from symbols.json for ::java::data::advancement::trigger::ConstructBeaconTrigger
Local link to file: generated_symbols/data/advancement/trigger/ConstructBeaconTrigger.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass

from generated_symbols.data.advancement.trigger.AllOptional import AllOptional
from generated_symbols.data.advancement.trigger.PlayerConditions import PlayerConditions
from generated_symbols.data.util.MinMaxBounds import MinMaxBounds


@dataclass(kw_only=True)
class ConstructBeaconTriggerTypeArg(PlayerConditions):
    level: MinMaxBounds[int] | int | None = None  # Tier of the updated beacon base.


ConstructBeaconTrigger = AllOptional[ConstructBeaconTriggerTypeArg]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::ConstructBeaconTrigger": {
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
                        "desc": "Tier of the updated beacon base.",
                        "key": "level",
                        "type": {
                            "kind": "concrete",
                            "child": {
                                "kind": "reference",
                                "path": "::java::data::util::MinMaxBounds"
                            },
                            "typeArgs": [
                                {
                                    "kind": "int"
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

