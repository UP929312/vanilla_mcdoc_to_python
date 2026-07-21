# Generated from symbols.json for ::java::world::entity::minecart::ChestMinecart
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated
from generated_symbols.world.entity.minecart.ContainerMinecart import ContainerMinecart
from generated_symbols.world.entity.minecart.Minecart import Minecart

if TYPE_CHECKING:
    from generated_symbols.util.slot.SlottedItem import SlottedItem


@dataclass(kw_only=True)
class ChestMinecart(Minecart, ContainerMinecart):
    Items: Annotated[list[SlottedItem[Annotated[int, 'Range | `0`-`26` | both inclusive']]], 'Length = 0-27 (both inclusive)'] | None = None  # Slots from 0 to 26.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::minecart::ChestMinecart": {
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
                "desc": "Slots from 0 to 26.",
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
                                    "max": 26
                                }
                            }
                        ]
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 27
                    }
                },
                "optional": True
            }
        ]
    }
}

