"""
Generated from symbols.json for ::java::world::entity::minecart::HopperMinecart
Local link to file: generated_symbols/world/entity/minecart/HopperMinecart.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from generated_symbols.world.entity.minecart.ContainerMinecart import ContainerMinecart
from generated_symbols.world.entity.minecart.Minecart import Minecart

if TYPE_CHECKING:
    from generated_symbols.util.slot.SlottedItem import SlottedItem


class HopperMinecart(ContainerMinecart, Minecart):
    Items: Annotated[list[SlottedItem[Annotated[int, Field(ge=0, le=4)]]], Field(min_length=0, max_length=5)] | None = None  # Slots from 0 to 4.
    TransferCooldown: int | None = None  # Ticks until an item can be transferred.
    Enabled: bool | None = None  # Whether it should pick up items.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::minecart::HopperMinecart": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::minecart::Minecart"
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::minecart::ContainerMinecart"
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
            },
            {
                "kind": "pair",
                "desc": "Whether it should pick up items.",
                "key": "Enabled",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}
