"""
Generated from symbols.json for ::java::world::entity::boat::ChestBoat
Local link to file: generated_symbols/world/entity/boat/ChestBoat.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

from generated_symbols.world.entity.boat.Boat import Boat
from runtime_metadata import IdSpec

if TYPE_CHECKING:
    from generated_symbols.util.slot.SlottedItem import SlottedItem


@dataclass(kw_only=True)
class ChestBoat(Boat):
    LootTable: Annotated[str, IdSpec(registry='loot_table', empty='allowed')] | None = None  # Loot table that will populate this chest boat.
    LootTableSeed: int | None = None  # Seed of the loot table.
    Items: Annotated[list[SlottedItem[Annotated[int, 'Range | `0`-`26` | both inclusive']]], 'Length = 0-27 (both inclusive)'] | None = None  # Slots from 0 to 26.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::boat::ChestBoat": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::boat::Boat"
                }
            },
            {
                "kind": "pair",
                "desc": "Loot table that will populate this chest boat.",
                "key": "LootTable",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "tree",
                                "values": {
                                    "registry": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "loot_table"
                                        }
                                    },
                                    "empty": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "allowed"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Seed of the loot table.",
                "key": "LootTableSeed",
                "type": {
                    "kind": "long",
                    "attributes": [
                        {
                            "name": "random"
                        }
                    ]
                },
                "optional": True
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

