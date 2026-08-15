"""
Generated from symbols.json for ::java::data::advancement::trigger::DefaultBlockInteractionTrigger
Local link to file: generated_symbols/data/advancement/trigger/DefaultBlockInteractionTrigger.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass

from generated_symbols.data.advancement.trigger.AdvancementLocationPredicate import AdvancementLocationPredicate
from generated_symbols.data.advancement.trigger.AllOptional import AllOptional
from generated_symbols.data.advancement.trigger.PlayerConditions import PlayerConditions


@dataclass(kw_only=True)
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

