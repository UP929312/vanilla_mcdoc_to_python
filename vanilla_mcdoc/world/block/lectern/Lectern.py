"""
Generated from symbols.json for ::java::world::block::lectern::Lectern
Local link to file: vanilla_mcdoc/world/block/lectern/Lectern.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.world.block.BlockEntity import BlockEntity

if TYPE_CHECKING:
    from vanilla_mcdoc.world.item.ItemStack import ItemStack


class Lectern(BlockEntity):
    Book: ItemStack | None = None
    Page: int | None = None  # Current page the book is on.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::lectern::Lectern": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::block::BlockEntity"
                }
            },
            {
                "kind": "pair",
                "key": "Book",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::item::ItemStack"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Current page the book is on.",
                "key": "Page",
                "type": {
                    "kind": "int"
                },
                "optional": True
            }
        ]
    }
}
