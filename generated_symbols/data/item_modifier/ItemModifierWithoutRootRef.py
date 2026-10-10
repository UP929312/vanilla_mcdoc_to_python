"""
Generated from symbols.json for ::java::data::item_modifier::ItemModifierWithoutRootRef
Local link to file: generated_symbols/data/item_modifier/ItemModifierWithoutRootRef.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.loot.LootFunction import LootFunction


type ItemModifierWithoutRootRef = LootFunction | list[ItemModifierWithoutRootRef]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::item_modifier::ItemModifierWithoutRootRef": {
        "kind": "union",
        "members": [
            {
                "kind": "reference",
                "path": "::java::data::loot::LootFunction"
            },
            {
                "kind": "list",
                "item": {
                    "kind": "reference",
                    "path": "::java::data::item_modifier::ItemModifierWithoutRootRef"
                }
            }
        ]
    }
}
