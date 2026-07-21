# Generated from symbols.json for ::java::world::block::container::Container9
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated
from generated_symbols.world.block.container.ContainerBase import ContainerBase

if TYPE_CHECKING:
    from generated_symbols.util.slot.SlottedItem import SlottedItem


@dataclass(kw_only=True)
class Container9(ContainerBase):
    Items: Annotated[list[SlottedItem[Annotated[int, 'Range | `0`-`8` | both inclusive']]], 'Length = 0-9 (both inclusive)'] | None = None  # Slots from 0 to 8.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::container::Container9": {
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
                "desc": "Slots from 0 to 8.",
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
                                    "max": 8
                                }
                            }
                        ]
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 9
                    }
                },
                "optional": True
            }
        ]
    }
}

