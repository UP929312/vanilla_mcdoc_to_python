# Generated from symbols.json for ::java::world::block::spawner::TrialSpawner
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.trial_spawner.TrialSpawnerConfig import TrialSpawnerConfig
    from generated_symbols.world.block.spawner.SpawnerEntry import SpawnerEntry


@dataclass(kw_only=True)
class TrialSpawner:
    normal_config: TrialSpawnerConfig | str | None = None  # Spawning behavior when the player does not have the Bad Omen effect.
    ominous_config: TrialSpawnerConfig | str | None = None  # Spawning behavior when the player has the Bad Omen effect.
    required_player_range: Annotated[int, 'Range | `1`-`128` | both inclusive'] | None = None  # Maximum distance for players to activate the trial spawner, or join a battle
    target_cooldown_length: int | None = None  # Time in ticks for the cooldown period. Included the time spend dispensing the reward.
    registered_players: list[tuple[int, int, int, int]] | None = None  # Players that are have been nearby during the current battle
    current_mobs: list[tuple[int, int, int, int]] | None = None  # All mobs that have been spawned by this trial spawner and are currently alive
    cooldown_ends_at: int | None = None  # Gametime in ticks when the cooldown ends
    next_mob_spawns_at: int | None = None  # Gametime in ticks when the next spawning attempt happens
    total_mobs_spawned: int | None = None
    spawn_data: SpawnerEntry | None = None  # The next entity to spawn, also controlls the entity displayed in the trial spawner
    ejecting_loot_table: str | None = None  # The loot table selected to be used to determine the reward


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::spawner::TrialSpawner": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Spawning behavior when the player does not have the Bad Omen effect.",
                "key": "normal_config",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "reference",
                            "path": "::java::data::trial_spawner::TrialSpawnerConfig"
                        },
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.21.2"
                                        }
                                    }
                                },
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "trial_spawner"
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
                "desc": "Spawning behavior when the player has the Bad Omen effect.",
                "key": "ominous_config",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "reference",
                            "path": "::java::data::trial_spawner::TrialSpawnerConfig"
                        },
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.21.2"
                                        }
                                    }
                                },
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "trial_spawner"
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
                "desc": "Maximum distance for players to activate the trial spawner, or join a battle",
                "key": "required_player_range",
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
                "desc": "Time in ticks for the cooldown period. Included the time spend dispensing the reward.",
                "key": "target_cooldown_length",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Players that are have been nearby during the current battle",
                "key": "registered_players",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "list",
                        "item": {
                            "kind": "int"
                        },
                        "lengthRange": {
                            "kind": 0,
                            "min": 4,
                            "max": 4
                        },
                        "attributes": [
                            {
                                "name": "uuid"
                            }
                        ]
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "All mobs that have been spawned by this trial spawner and are currently alive",
                "key": "current_mobs",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "list",
                        "item": {
                            "kind": "int"
                        },
                        "lengthRange": {
                            "kind": 0,
                            "min": 4,
                            "max": 4
                        },
                        "attributes": [
                            {
                                "name": "uuid"
                            }
                        ]
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Gametime in ticks when the cooldown ends",
                "key": "cooldown_ends_at",
                "type": {
                    "kind": "long"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Gametime in ticks when the next spawning attempt happens",
                "key": "next_mob_spawns_at",
                "type": {
                    "kind": "long"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "total_mobs_spawned",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "The next entity to spawn, also controlls the entity displayed in the trial spawner",
                "key": "spawn_data",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::block::spawner::SpawnerEntry"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "The loot table selected to be used to determine the reward",
                "key": "ejecting_loot_table",
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

