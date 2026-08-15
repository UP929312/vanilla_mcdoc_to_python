"""
Generated from symbols.json for ::java::world::item::ItemStack
Local link to file: generated_symbols/world/item/ItemStack.py
"""
# ~~~ CODE ~~~
from generated_symbols.world.component.DataComponentPatch import DataComponentPatch
from generated_symbols.world.item.ItemStackOfComponent import ItemStackOfComponent


ItemStack = ItemStackOfComponent[DataComponentPatch]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::item::ItemStack": {
        "kind": "concrete",
        "child": {
            "kind": "reference",
            "path": "::java::world::item::ItemStackOfComponent"
        },
        "typeArgs": [
            {
                "kind": "reference",
                "path": "::java::world::component::DataComponentPatch"
            }
        ]
    }
}

