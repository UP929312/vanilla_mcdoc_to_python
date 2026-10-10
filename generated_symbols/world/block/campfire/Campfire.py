"""
Generated from symbols.json for ::java::world::block::campfire::Campfire
Local link to file: generated_symbols/world/block/campfire/Campfire.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from generated_symbols.world.block.BlockEntity import BlockEntity

if TYPE_CHECKING:
    from generated_symbols.util.slot.SlottedItem import SlottedItem


class Campfire(BlockEntity):
    Items: Annotated[list[SlottedItem[Annotated[int, Field(ge=0, le=3)]]], Field(min_length=0, max_length=4)] | None = None
    CookingTimes: tuple[int, int, int, int] | None = None  # Ticks each item has been cooking. Index is according to item slot.
    CookingTotalTimes: tuple[int, int, int, int] | None = None  # Ticks each item still has to cook. Index is according to item slot.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::campfire::Campfire": {
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
                                    "max": 3
                                }
                            }
                        ]
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 4
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Ticks each item has been cooking.\nIndex is according to item slot.",
                "key": "CookingTimes",
                "type": {
                    "kind": "int_array",
                    "lengthRange": {
                        "kind": 0,
                        "min": 4,
                        "max": 4
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Ticks each item still has to cook.\nIndex is according to item slot.",
                "key": "CookingTotalTimes",
                "type": {
                    "kind": "int_array",
                    "lengthRange": {
                        "kind": 0,
                        "min": 4,
                        "max": 4
                    }
                },
                "optional": True
            }
        ]
    }
}
