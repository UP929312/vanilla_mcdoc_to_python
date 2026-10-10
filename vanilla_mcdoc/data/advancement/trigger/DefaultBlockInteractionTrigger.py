"""
Generated from symbols.json for ::java::data::advancement::trigger::DefaultBlockInteractionTrigger
Local link to file: vanilla_mcdoc/data/advancement/trigger/DefaultBlockInteractionTrigger.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.data.advancement.trigger.AdvancementLocationPredicate import AdvancementLocationPredicate
from vanilla_mcdoc.data.advancement.trigger.AllOptional import AllOptional
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions


class DefaultBlockInteractionTriggerTypeArg(PlayerConditions):
    location: AdvancementLocationPredicate | None = None  # Predicate context: Block Use.


DefaultBlockInteractionTrigger = AllOptional[DefaultBlockInteractionTriggerTypeArg]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::DefaultBlockInteractionTrigger": {
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
                        "desc": "Predicate context: Block Use.",
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
