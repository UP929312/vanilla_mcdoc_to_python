"""
Generated from symbols.json for ::java::world::block::container::Shelf
Local link to file: generated_symbols/world/block/container/Shelf.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from generated_symbols.world.block.container.ContainerBase import ContainerBase

if TYPE_CHECKING:
    from generated_symbols.util.slot.SlottedItem import SlottedItem


class Shelf(ContainerBase):
    Items: Annotated[list[SlottedItem[Annotated[int, Field(ge=0, le=2)]]], Field(min_length=0, max_length=3)] | None = None  # Slots from 0 to 2.
    align_items_to_bottom: bool | None = None  # Defaults to `false`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::container::Shelf": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::block::container::ContainerBase"
                }
            },
            {
                "kind": "pair",
                "desc": "Slots from 0 to 2.",
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
                                    "max": 2
                                }
                            }
                        ]
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 3
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Defaults to `False`.",
                "key": "align_items_to_bottom",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}
