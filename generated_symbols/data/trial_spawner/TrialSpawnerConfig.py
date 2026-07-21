# Generated from symbols.json for ::java::data::trial_spawner::TrialSpawnerConfig
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.util.WeightedList import WeightedList
    from generated_symbols.world.block.spawner.SpawnPotential import SpawnPotential


@dataclass(kw_only=True)
class TrialSpawnerConfig:
    spawn_range: Annotated[int, 'Range | `1`-`128` | both inclusive'] | None = None  # Maximum distance from the spawner that en entity can spawn
    total_mobs: float | None = None  # Total amount of entities that are spawned during one activation, when 1 player is nearby
    total_mobs_added_per_player: float | None = None  # Number added to `total_mobs` for each additional player
    simultaneous_mobs: float | None = None  # Number of entities that that can be present at once, when 1 player is nearby
    simultaneous_mobs_added_per_player: float | None = None  # Number added to `simultaneous_mobs` for each additional player
    ticks_between_spawn: int | None = None  # Ticks until the next spawn.
    spawn_potentials: list[SpawnPotential] | None = None  # Entities that can be placed.
    loot_tables_to_eject: WeightedList[str] | None = None  # Loot tables to use when ejecting loot. Chooses one loot table based on weight and then uses it as often as there are players nearby.
    items_to_drop_when_ominous: str | None = None  # Loot table to use when summoning ominous item spawners. One roll seeded based on rough location to determine all items used during the battle.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::trial_spawner::TrialSpawnerConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Maximum distance from the spawner that en entity can spawn",
                "key": "spawn_range",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1,
                        "max": 128
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Total amount of entities that are spawned during one activation, when 1 player is nearby",
                "key": "total_mobs",
                "type": {
                    "kind": "float"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Number added to `total_mobs` for each additional player",
                "key": "total_mobs_added_per_player",
                "type": {
                    "kind": "float"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Number of entities that that can be present at once, when 1 player is nearby",
                "key": "simultaneous_mobs",
                "type": {
                    "kind": "float"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Number added to `simultaneous_mobs` for each additional player",
                "key": "simultaneous_mobs_added_per_player",
                "type": {
                    "kind": "float"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Ticks until the next spawn.",
                "key": "ticks_between_spawn",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Entities that can be placed.",
                "key": "spawn_potentials",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::world::block::spawner::SpawnPotential"
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Loot tables to use when ejecting loot. Chooses one loot table based on weight and then uses it as often as there are players nearby.",
                "key": "loot_tables_to_eject",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::util::WeightedList"
                    },
                    "typeArgs": [
                        {
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
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Loot table to use when summoning ominous item spawners. One roll seeded based on rough location to determine all items used during the battle.",
                "key": "items_to_drop_when_ominous",
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
                },
                "optional": True
            }
        ]
    }
}

