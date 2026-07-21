# Generated from symbols.json for ::java::world::block::container::Hopper
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated
from generated_symbols.world.block.container.ContainerBase import ContainerBase

if TYPE_CHECKING:
    from generated_symbols.util.slot.SlottedItem import SlottedItem


@dataclass(kw_only=True)
class Hopper(ContainerBase):
    Items: Annotated[list[SlottedItem[Annotated[int, 'Range | `0`-`4` | both inclusive']]], 'Length = 0-5 (both inclusive)'] | None = None  # Slots from 0 to 4.
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

