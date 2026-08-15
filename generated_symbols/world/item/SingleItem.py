"""
Generated from symbols.json for ::java::world::item::SingleItem
Local link to file: generated_symbols/world/item/SingleItem.py
"""
# ~~~ CODE ~~~
from generated_symbols.world.component.DataComponentPatch import DataComponentPatch
from generated_symbols.world.item.SingleItemOfComponent import SingleItemOfComponent


SingleItem = SingleItemOfComponent[DataComponentPatch]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::item::SingleItem": {
        "kind": "concrete",
        "child": {
            "kind": "reference",
            "path": "::java::world::item::SingleItemOfComponent"
        },
        "typeArgs": [
            {
                "kind": "reference",
                "path": "::java::world::component::DataComponentPatch"
            }
        ]
    }
}

