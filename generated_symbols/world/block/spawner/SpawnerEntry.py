# Generated from symbols.json for ::java::world::block::spawner::SpawnerEntry
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.world.block.spawner.CustomSpawnRules import CustomSpawnRules
    from generated_symbols.world.block.spawner.SpawnEquipment import SpawnEquipment
    from generated_symbols.world.entity.AnyEntity import AnyEntity


@dataclass(kw_only=True)
class SpawnerEntry:
    entity: AnyEntity
    custom_spawn_rules: CustomSpawnRules | None = None
    equipment: SpawnEquipment | None = None  # Rolled items from the specified loot table will be equipped to the mob that spawns.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::spawner::SpawnerEntry": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "entity",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::AnyEntity"
                }
            },
            {
                "kind": "pair",
                "key": "custom_spawn_rules",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::block::spawner::CustomSpawnRules"
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
                                "value": "1.20.5"
                            }
                        }
                    }
                ],
                "desc": "Rolled items from the specified loot table will be equipped to the mob that spawns.",
                "key": "equipment",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::block::spawner::SpawnEquipment"
                },
                "optional": True
            }
        ]
    }
}

