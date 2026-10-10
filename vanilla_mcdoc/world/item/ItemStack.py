"""
Generated from symbols.json for ::java::world::item::ItemStack
Local link to file: vanilla_mcdoc/world/item/ItemStack.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.world.component.DataComponentPatch import DataComponentPatch
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent


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
