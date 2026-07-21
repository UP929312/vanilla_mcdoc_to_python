# Generated from symbols.json for ::java::world::item::ItemStack
from typing import TYPE_CHECKING

if TYPE_CHECKING:
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

