"""
Generated from symbols.json for ::java::data::advancement::trigger::EnchantedItemTrigger
Local link to file: generated_symbols/data/advancement/trigger/EnchantedItemTrigger.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass

from generated_symbols.data.advancement.predicate.ItemPredicate import ItemPredicate
from generated_symbols.data.advancement.trigger.AllOptional import AllOptional
from generated_symbols.data.advancement.trigger.PlayerConditions import PlayerConditions
from generated_symbols.data.util.MinMaxBounds import MinMaxBounds


@dataclass(kw_only=True)
class EnchantedItemTriggerTypeArg(PlayerConditions):
    item: ItemPredicate | None = None
    levels: MinMaxBounds[int] | int | None = None


EnchantedItemTrigger = AllOptional[EnchantedItemTriggerTypeArg]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::EnchantedItemTrigger": {
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
                        "key": "levels",
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

