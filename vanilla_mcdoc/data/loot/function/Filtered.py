"""
Generated from symbols.json for ::java::data::loot::function::Filtered
Local link to file: vanilla_mcdoc/data/loot/function/Filtered.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.data.loot.function.Conditions import Conditions

if TYPE_CHECKING:
    from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
    from vanilla_mcdoc.data.item_modifier.ItemModifier import ItemModifier


class Filtered(Conditions):
    item_filter: ItemPredicate  # Item predicate to select items to modify.
    on_pass: ItemModifier | None = None  # Loot function to apply to the item when `item_filter` passes.
    on_fail: ItemModifier | None = None  # Loot function to apply to the item when `item_filter` fails.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::Filtered": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Item predicate to select items to modify.",
                "key": "item_filter",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::ItemPredicate"
                }
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.11"
                            }
                        }
                    }
                ],
                "desc": "Loot function to apply to the selected items.",
                "key": "modifier",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::item_modifier::ItemModifier"
                }
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.11"
                            }
                        }
                    }
                ],
                "desc": "Loot function to apply to the item when `item_filter` passes.",
                "key": "on_pass",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::item_modifier::ItemModifier"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.11"
                            }
                        }
                    }
                ],
                "desc": "Loot function to apply to the item when `item_filter` fails.",
                "key": "on_fail",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::item_modifier::ItemModifier"
                },
                "optional": True
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::loot::function::Conditions"
                }
            }
        ]
    }
}
