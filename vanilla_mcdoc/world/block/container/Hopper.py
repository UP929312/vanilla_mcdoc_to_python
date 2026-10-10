"""
Generated from symbols.json for ::java::world::block::container::Hopper
Local link to file: vanilla_mcdoc/world/block/container/Hopper.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.world.block.container.ContainerBase import ContainerBase

if TYPE_CHECKING:
    from vanilla_mcdoc.util.slot.SlottedItem import SlottedItem


class Hopper(ContainerBase):
    Items: Annotated[list[SlottedItem[Annotated[int, Field(ge=0, le=4)]]], Field(min_length=0, max_length=5)] | None = None  # Slots from 0 to 4.
    TransferCooldown: int | None = None  # Ticks until an item can be transferred.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::container::Hopper": {
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
                "desc": "Slots from 0 to 4.",
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
                                    "max": 4
                                }
                            }
                        ]
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 5
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Ticks until an item can be transferred.",
                "key": "TransferCooldown",
                "type": {
                    "kind": "int"
                },
                "optional": True
            }
        ]
    }
}
