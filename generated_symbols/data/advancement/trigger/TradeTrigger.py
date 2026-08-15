"""
Generated from symbols.json for ::java::data::advancement::trigger::TradeTrigger
Local link to file: generated_symbols/data/advancement/trigger/TradeTrigger.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass

from generated_symbols.data.advancement.predicate.ItemPredicate import ItemPredicate
from generated_symbols.data.advancement.trigger.AdvancementEntityPredicate import AdvancementEntityPredicate
from generated_symbols.data.advancement.trigger.AllOptional import AllOptional
from generated_symbols.data.advancement.trigger.PlayerConditions import PlayerConditions


@dataclass(kw_only=True)
class TradeTriggerTypeArg(PlayerConditions):
    villager: AdvancementEntityPredicate | None = None  # Predicate context: Advancement Entity.
    item: ItemPredicate | None = None  # Item that was purchased.  `count` tag checks the item count from one trade, not the total amount traded for.


TradeTrigger = AllOptional[TradeTriggerTypeArg]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::TradeTrigger": {
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
                        "desc": "Predicate context: Advancement Entity.",
                        "key": "villager",
                        "type": {
                            "kind": "reference",
                            "path": "::java::data::advancement::trigger::AdvancementEntityPredicate"
                        },
                        "optional": True
                    },
                    {
                        "kind": "pair",
                        "desc": "Item that was purchased. \\\n`count` tag checks the item count from one trade, not the total amount traded for.",
                        "key": "item",
                        "type": {
                            "kind": "reference",
                            "path": "::java::data::advancement::predicate::ItemPredicate"
                        },
                        "optional": True
                    }
                ]
            }
        ]
    }
}

