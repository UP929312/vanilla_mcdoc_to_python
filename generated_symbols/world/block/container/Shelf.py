# Generated from symbols.json for ::java::world::block::container::Shelf
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated
from generated_symbols.world.block.container.ContainerBase import ContainerBase

if TYPE_CHECKING:
    from generated_symbols.util.slot.SlottedItem import SlottedItem


@dataclass(kw_only=True)
class Shelf(ContainerBase):
    Items: Annotated[list[SlottedItem[Annotated[int, 'Range | `0`-`2` | both inclusive']]], 'Length = 0-3 (both inclusive)'] | None = None  # Slots from 0 to 2.
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

