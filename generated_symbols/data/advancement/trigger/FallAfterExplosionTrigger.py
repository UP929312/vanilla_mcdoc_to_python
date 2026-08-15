"""
Generated from symbols.json for ::java::data::advancement::trigger::FallAfterExplosionTrigger
Local link to file: generated_symbols/data/advancement/trigger/FallAfterExplosionTrigger.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass

from generated_symbols.data.advancement.predicate.DistancePredicate import DistancePredicate
from generated_symbols.data.advancement.predicate.LocationPredicate import LocationPredicate
from generated_symbols.data.advancement.trigger.AdvancementEntityPredicate import AdvancementEntityPredicate
from generated_symbols.data.advancement.trigger.AllOptional import AllOptional
from generated_symbols.data.advancement.trigger.PlayerConditions import PlayerConditions


@dataclass(kw_only=True)
class FallAfterExplosionTriggerTypeArg(PlayerConditions):
    start_position: LocationPredicate | None = None
    distance: DistancePredicate | None = None
    cause: AdvancementEntityPredicate | None = None  # Predicate context: Advancement Entity.  Entity may not exist.


FallAfterExplosionTrigger = AllOptional[FallAfterExplosionTriggerTypeArg]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::FallAfterExplosionTrigger": {
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
                        "key": "start_position",
                        "type": {
                            "kind": "reference",
                            "path": "::java::data::advancement::predicate::LocationPredicate"
                        },
                        "optional": True
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
                        "desc": "Predicate context: Advancement Entity. \\\nEntity may not exist.",
                        "key": "cause",
                        "type": {
                            "kind": "reference",
                            "path": "::java::data::advancement::trigger::AdvancementEntityPredicate"
                        },
                        "optional": True
                    }
                ]
            }
        ]
    }
}

