# Generated from symbols.json for ::java::world::entity::item_frame::ItemFrame
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated
from generated_symbols.world.entity.BlockAttachedEntity import BlockAttachedEntity

if TYPE_CHECKING:
    from generated_symbols.world.entity.item_frame.Facing import Facing
    from generated_symbols.world.item.ItemStack import ItemStack


@dataclass(kw_only=True)
class ItemFrame(BlockAttachedEntity):
    Facing: Facing | None = None  # Direction it is facing.
    Item: ItemStack | None = None
    ItemDropChance: float | None = None  # Chance the item has to drop.
    ItemRotation: Annotated[int, 'Range | `0`-`7` | both inclusive'] | None = None  # Rotation of the item.
    Invisible: bool | None = None  # Whether the item frame should be invisible. The item inside the frame is not effected.
    Fixed: bool | None = None  # Whether the item frame should not be able to be broken and should disallow the item to be moved.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::item_frame::ItemFrame": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::BlockAttachedEntity"
                }
            },
            {
                "kind": "pair",
                "desc": "Direction it is facing.",
                "key": "Facing",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::item_frame::Facing"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "Item",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::item::ItemStack"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Chance the item has to drop.",
                "key": "ItemDropChance",
                "type": {
                    "kind": "float"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Rotation of the item.",
                "key": "ItemRotation",
                "type": {
                    "kind": "byte",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 7
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.16"
                            }
                        }
                    }
                ],
                "desc": "Whether the item frame should be invisible.\nThe item inside the frame is not effected.",
                "key": "Invisible",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.16"
                            }
                        }
                    }
                ],
                "desc": "Whether the item frame should not be able to be broken and should disallow the item to be moved.",
                "key": "Fixed",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

