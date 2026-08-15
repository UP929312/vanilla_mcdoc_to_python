"""
Generated from symbols.json for ::java::data::advancement::trigger::ItemDurabilityTrigger
Local link to file: generated_symbols/data/advancement/trigger/ItemDurabilityTrigger.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass

from generated_symbols.data.advancement.predicate.ItemPredicate import ItemPredicate
from generated_symbols.data.advancement.trigger.AllOptional import AllOptional
from generated_symbols.data.advancement.trigger.PlayerConditions import PlayerConditions
from generated_symbols.data.util.MinMaxBounds import MinMaxBounds


@dataclass(kw_only=True)
class ItemDurabilityTriggerTypeArg(PlayerConditions):
    delta: MinMaxBounds[int] | int | None = None  # Change in durability (negative numbers are used to indicate a decrease in durability).
    durability: MinMaxBounds[int] | int | None = None  # The resulting durability.
    item: ItemPredicate | None = None  # The item before its durability changed.


ItemDurabilityTrigger = AllOptional[ItemDurabilityTriggerTypeArg]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::ItemDurabilityTrigger": {
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
                        "desc": "Change in durability (negative numbers are used to indicate a decrease in durability).",
                        "key": "delta",
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
                    },
                    {
                        "kind": "pair",
                        "desc": "The resulting durability.",
                        "key": "durability",
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
                    },
                    {
                        "kind": "pair",
                        "desc": "The item before its durability changed.",
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

