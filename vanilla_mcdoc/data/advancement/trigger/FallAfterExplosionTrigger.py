"""
Generated from symbols.json for ::java::data::advancement::trigger::FallAfterExplosionTrigger
Local link to file: vanilla_mcdoc/data/advancement/trigger/FallAfterExplosionTrigger.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.data.advancement.predicate.DistancePredicate import DistancePredicate
from vanilla_mcdoc.data.advancement.predicate.LocationPredicate import LocationPredicate
from vanilla_mcdoc.data.advancement.trigger.AdvancementEntityPredicate import AdvancementEntityPredicate
from vanilla_mcdoc.data.advancement.trigger.AllOptional import AllOptional
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions


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
