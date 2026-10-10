"""
Generated from symbols.json for ::java::world::block::chiseled_bookshelf::ChiseledBookshelf
Local link to file: generated_symbols/world/block/chiseled_bookshelf/ChiseledBookshelf.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from generated_symbols.world.block.BlockEntity import BlockEntity

if TYPE_CHECKING:
    from generated_symbols.util.slot.SlottedItem import SlottedItem


class ChiseledBookshelf(BlockEntity):
    Items: Annotated[list[SlottedItem[Annotated[int, Field(ge=0, le=5)]]], Field(min_length=0, max_length=6)] | None = None  # Slots from 0 to 5.
    last_interacted_slot: Annotated[int, Field(ge=0, le=5)] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::chiseled_bookshelf::ChiseledBookshelf": {
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
                "desc": "Slots from 0 to 5.",
                "key": "Items",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "concrete",
                        "child": {
                            "kind": "reference",
                            "path": "::java::util::slot::SlottedItem"
                        },
                        "typeArgs": [
                            {
                                "kind": "byte",
                                "valueRange": {
                                    "kind": 0,
                                    "min": 0,
                                    "max": 5
                                }
                            }
                        ]
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 6
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "last_interacted_slot",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 5
                    }
                },
                "optional": True
            }
        ]
    }
}
