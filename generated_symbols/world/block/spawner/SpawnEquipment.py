# Generated from symbols.json for ::java::world::block::spawner::SpawnEquipment
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.util.slot.EquipmentSlot import EquipmentSlot


@dataclass(kw_only=True)
class SpawnEquipment:
    loot_table: str  # Generates the equipment.
    slot_drop_chances: Annotated[float, 'Range | `0`-`1` | both inclusive'] | dict[EquipmentSlot, Annotated[float, 'Range | `0`-`1` | both inclusive']]  # Chance the mob will drop the equipment on death.


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

