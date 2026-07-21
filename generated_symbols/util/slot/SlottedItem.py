# Generated from symbols.json for ::java::util::slot::SlottedItem
from dataclasses import dataclass
from typing import Generic, TypeVar
from generated_symbols.world.item.ItemStack import ItemStack


T = TypeVar('T')

@dataclass(kw_only=True)
class SlottedItem(ItemStack, Generic[T]):
    Slot: T | None = None  # Inventory slot the item is in


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::slot::SlottedItem": {
        "kind": "template",
        "child": {
            "kind": "struct",
            "fields": [
                {
                    "kind": "spread",
                    "type": {
                        "kind": "reference",
                        "path": "::java::world::item::ItemStack"
                    }
                },
                {
                    "kind": "pair",
                    "desc": "Inventory slot the item is in",
                    "key": "Slot",
                    "type": {
                        "kind": "reference",
                        "path": "::java::util::slot::T"
                    },
                    "optional": True
                }
            ]
        },
        "typeParams": [
            {
                "path": "::java::util::slot::T"
            }
        ]
    }
}

