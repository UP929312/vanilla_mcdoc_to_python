"""
Generated from symbols.json for ::java::data::advancement::trigger::ChanneledLightningTrigger
Local link to file: generated_symbols/data/advancement/trigger/ChanneledLightningTrigger.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass

from generated_symbols.data.advancement.trigger.AdvancementEntityPredicate import AdvancementEntityPredicate
from generated_symbols.data.advancement.trigger.AllOptional import AllOptional
from generated_symbols.data.advancement.trigger.PlayerConditions import PlayerConditions


@dataclass(kw_only=True)
class ChanneledLightningTriggerTypeArg(PlayerConditions):
    victims: list[AdvancementEntityPredicate] | None = None  # Predicate context: Advancement Entity.  Evaluates to true if every predicate in the list matches some victims.


ChanneledLightningTrigger = AllOptional[ChanneledLightningTriggerTypeArg]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::ChanneledLightningTrigger": {
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
                        "desc": "Predicate context: Advancement Entity. \\\nEvaluates to True if every predicate in the list matches some victims.",
                        "key": "victims",
                        "type": {
                            "kind": "list",
                            "item": {
                                "kind": "reference",
                                "path": "::java::data::advancement::trigger::AdvancementEntityPredicate"
                            }
                        },
                        "optional": True
                    }
                ]
            }
        ]
    }
}

