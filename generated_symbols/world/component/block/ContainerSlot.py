"""
Generated from symbols.json for ::java::world::component::block::ContainerSlot
Local link to file: generated_symbols/world/component/block/ContainerSlot.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.world.item.ItemStackTemplate import ItemStackTemplate


class ContainerSlot(GeneratedModel):
    slot: Annotated[int, Field(ge=0, le=255)]  # The slot ID of the container.
    item: ItemStackTemplate  # The item stack in this container slot.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::block::ContainerSlot": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The slot ID of the container.",
                "key": "slot",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 255
                    }
                }
            },
            {
                "kind": "pair",
                "desc": "The item stack in this container slot.",
                "key": "item",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::item::ItemStackTemplate"
                }
            }
        ]
    }
}

