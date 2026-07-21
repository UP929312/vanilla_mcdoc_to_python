# Generated from symbols.json for ::java::world::block::lectern::Lectern
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.block.BlockEntity import BlockEntity

if TYPE_CHECKING:
    from generated_symbols.world.item.ItemStack import ItemStack


@dataclass(kw_only=True)
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

