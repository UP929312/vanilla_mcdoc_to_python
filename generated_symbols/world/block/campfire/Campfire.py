# Generated from symbols.json for ::java::world::block::campfire::Campfire
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated
from generated_symbols.world.block.BlockEntity import BlockEntity

if TYPE_CHECKING:
    from generated_symbols.util.slot.SlottedItem import SlottedItem


@dataclass(kw_only=True)
class Campfire(BlockEntity):
    Items: Annotated[list[SlottedItem[Annotated[int, 'Range | `0`-`3` | both inclusive']]], 'Length = 0-4 (both inclusive)'] | None = None
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

