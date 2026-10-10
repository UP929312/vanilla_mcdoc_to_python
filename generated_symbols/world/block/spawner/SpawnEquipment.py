"""
Generated from symbols.json for ::java::world::block::spawner::SpawnEquipment
Local link to file: generated_symbols/world/block/spawner/SpawnEquipment.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel
from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.util.slot.EquipmentSlot import EquipmentSlot


class SpawnEquipment(GeneratedModel):
    loot_table: Annotated[str, IdSpec(registry='loot_table')]  # Generates the equipment.
    slot_drop_chances: Annotated[float, Field(ge=0, le=1)] | dict[EquipmentSlot, Annotated[float, Field(ge=0, le=1)]]  # Chance the mob will drop the equipment on death.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::spawner::SpawnEquipment": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Generates the equipment.",
                "key": "loot_table",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "loot_table"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "desc": "Chance the mob will drop the equipment on death.",
                "key": "slot_drop_chances",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "float",
                            "valueRange": {
                                "kind": 0,
                                "min": 0,
                                "max": 1
                            }
                        },
                        {
                            "kind": "struct",
                            "fields": [
                                {
                                    "kind": "pair",
                                    "key": {
                                        "kind": "reference",
                                        "path": "::java::util::slot::EquipmentSlot"
                                    },
                                    "type": {
                                        "kind": "float",
                                        "valueRange": {
                                            "kind": 0,
                                            "min": 0,
                                            "max": 1
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                }
            }
        ]
    }
}

