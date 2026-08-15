"""
Generated from symbols.json for ::java::data::advancement::trigger::DistanceTrigger
Local link to file: generated_symbols/data/advancement/trigger/DistanceTrigger.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass

from generated_symbols.data.advancement.predicate.DistancePredicate import DistancePredicate
from generated_symbols.data.advancement.predicate.LocationPredicate import LocationPredicate
from generated_symbols.data.advancement.trigger.AllOptional import AllOptional
from generated_symbols.data.advancement.trigger.PlayerConditions import PlayerConditions


@dataclass(kw_only=True)
class DistanceTriggerTypeArg(PlayerConditions):
    start_position: LocationPredicate | None = None  # Where the player started to travel.
    distance: DistancePredicate | None = None  # How far the player travels.


DistanceTrigger = AllOptional[DistanceTriggerTypeArg]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::DistanceTrigger": {
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
                        "desc": "Where the player started to travel.",
                        "key": "start_position",
                        "type": {
                            "kind": "reference",
                            "path": "::java::data::advancement::predicate::LocationPredicate"
                        },
                        "optional": True
                    },
                    {
                        "kind": "pair",
                        "desc": "How far the player travels.",
                        "key": "distance",
                        "type": {
                            "kind": "reference",
                            "path": "::java::data::advancement::predicate::DistancePredicate"
                        },
                        "optional": True
                    }
                ]
            }
        ]
    }
}

