# Generated from symbols.json for ::java::world::item::ItemCost
from typing import TYPE_CHECKING

if TYPE_CHECKING:
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

