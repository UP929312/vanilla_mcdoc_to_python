# Generated from symbols.json for ::java::data::advancement::trigger::ItemDurabilityChanged
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.advancement.trigger.TriggerBase import TriggerBase

if TYPE_CHECKING:
    from generated_symbols.data.advancement.predicate.ItemPredicate import ItemPredicate
    from generated_symbols.data.util.MinMaxBounds import MinMaxBounds


@dataclass(kw_only=True)
class ItemDurabilityChanged(TriggerBase):
    delta: MinMaxBounds[int] | int | None = None  # Change in durability (negative numbers are used to indicate a decrease in durability).
    durability: MinMaxBounds[int] | int | None = None  # The resulting durability.
    item: ItemPredicate | None = None  # The item before its durability changed.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::ItemDurabilityChanged": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::trigger::TriggerBase"
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
}

