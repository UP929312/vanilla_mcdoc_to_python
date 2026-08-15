"""
Generated from symbols.json for ::java::world::item::ItemCost
Local link to file: generated_symbols/world/item/ItemCost.py
"""
# ~~~ CODE ~~~
from generated_symbols.world.component.DataComponentExactPredicate import DataComponentExactPredicate
from generated_symbols.world.item.ItemStackOfComponent import ItemStackOfComponent


ItemCost = ItemStackOfComponent[DataComponentExactPredicate]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::item::ItemCost": {
        "kind": "concrete",
        "child": {
            "kind": "reference",
            "path": "::java::world::item::ItemStackOfComponent"
        },
        "typeArgs": [
            {
                "kind": "reference",
                "path": "::java::world::component::DataComponentExactPredicate"
            }
        ]
    }
}

