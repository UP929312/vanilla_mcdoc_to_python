# Generated from symbols.json for ::java::world::component::block::ContainerSlot
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.world.item.ItemStackTemplate import ItemStackTemplate


@dataclass(kw_only=True)
class ContainerSlot:
    slot: Annotated[int, 'Range | `0`-`255` | both inclusive']  # The slot ID of the container.
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

