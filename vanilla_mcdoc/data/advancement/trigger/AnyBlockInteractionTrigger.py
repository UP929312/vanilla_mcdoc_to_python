"""
Generated from symbols.json for ::java::data::advancement::trigger::AnyBlockInteractionTrigger
Local link to file: vanilla_mcdoc/data/advancement/trigger/AnyBlockInteractionTrigger.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.data.advancement.trigger.AdvancementLocationPredicate import AdvancementLocationPredicate
from vanilla_mcdoc.data.advancement.trigger.AllOptional import AllOptional
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions


class AnyBlockInteractionTriggerTypeArg(PlayerConditions):
    location: AdvancementLocationPredicate | None = None  # Predicate context: Advancement Location.


AnyBlockInteractionTrigger = AllOptional[AnyBlockInteractionTriggerTypeArg]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::AnyBlockInteractionTrigger": {
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
                        "desc": "Predicate context: Advancement Location.",
                        "key": "location",
                        "type": {
                            "kind": "reference",
                            "path": "::java::data::advancement::trigger::AdvancementLocationPredicate"
                        },
                        "optional": True
                    }
                ]
            }
        ]
    }
}
