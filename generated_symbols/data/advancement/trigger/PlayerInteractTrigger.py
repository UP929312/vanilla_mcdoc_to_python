"""
Generated from symbols.json for ::java::data::advancement::trigger::PlayerInteractTrigger
Local link to file: generated_symbols/data/advancement/trigger/PlayerInteractTrigger.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass

from generated_symbols.data.advancement.predicate.ItemPredicate import ItemPredicate
from generated_symbols.data.advancement.trigger.AdvancementEntityPredicate import AdvancementEntityPredicate
from generated_symbols.data.advancement.trigger.AllOptional import AllOptional
from generated_symbols.data.advancement.trigger.PlayerConditions import PlayerConditions


@dataclass(kw_only=True)
class PlayerInteractTriggerTypeArg(PlayerConditions):
    item: ItemPredicate | None = None
    entity: AdvancementEntityPredicate | None = None  # Predicate context: Advancement Entity.


PlayerInteractTrigger = AllOptional[PlayerInteractTriggerTypeArg]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::PlayerInteractTrigger": {
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
                        "key": "item",
                        "type": {
                            "kind": "reference",
                            "path": "::java::data::advancement::predicate::ItemPredicate"
                        },
                        "optional": True
                    },
                    {
                        "kind": "pair",
                        "desc": "Predicate context: Advancement Entity.",
                        "key": "entity",
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

