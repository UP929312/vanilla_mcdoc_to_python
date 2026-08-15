"""
Generated from symbols.json for ::java::data::advancement::trigger::LevitationTrigger
Local link to file: generated_symbols/data/advancement/trigger/LevitationTrigger.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass

from generated_symbols.data.advancement.predicate.DistancePredicate import DistancePredicate
from generated_symbols.data.advancement.trigger.AllOptional import AllOptional
from generated_symbols.data.advancement.trigger.PlayerConditions import PlayerConditions
from generated_symbols.data.util.MinMaxBounds import MinMaxBounds


@dataclass(kw_only=True)
class LevitationTriggerTypeArg(PlayerConditions):
    distance: DistancePredicate | None = None
    duration: MinMaxBounds[int] | int | None = None


LevitationTrigger = AllOptional[LevitationTriggerTypeArg]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::LevitationTrigger": {
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
                        "key": "distance",
                        "type": {
                            "kind": "reference",
                            "path": "::java::data::advancement::predicate::DistancePredicate"
                        },
                        "optional": True
                    },
                    {
                        "kind": "pair",
                        "key": "duration",
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

