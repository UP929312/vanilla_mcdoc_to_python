# Generated from symbols.json for ::java::world::entity::mob::player::Player
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated
from generated_symbols.world.entity.mob.LivingEntity import LivingEntity

if TYPE_CHECKING:
    from generated_symbols.util.GlobalPos import GlobalPos
    from generated_symbols.util.slot.SlottedItem import SlottedItem
    from generated_symbols.world.entity.AnyEntity import AnyEntity
    from generated_symbols.world.entity.mob.player.Abilities import Abilities
    from generated_symbols.world.entity.mob.player.EnderPearl import EnderPearl
    from generated_symbols.world.entity.mob.player.Gamemode import Gamemode
    from generated_symbols.world.entity.mob.player.PlayerEquipment import PlayerEquipment
    from generated_symbols.world.entity.mob.player.PlayerSlot import PlayerSlot
    from generated_symbols.world.entity.mob.player.RecipeBook import RecipeBook
    from generated_symbols.world.entity.mob.player.Respawn import Respawn
    from generated_symbols.world.entity.mob.player.RootVehicle import RootVehicle
    from generated_symbols.world.entity.mob.player.WardenSpawnTracker import WardenSpawnTracker


@dataclass(kw_only=True)
class Player(LivingEntity):
    DataVersion: int | None = None  # Version of the player NBT structure
    Dimension: str | None = None
    LastDeathLocation: GlobalPos | None = None  # Location of the player's last death.
    playerGameType: Gamemode | None = None  # Game mode that the player is in.
    previousPlayerGameType: Gamemode | None = None  # Previous game mode that the player was in.
    Score: int | None = None  # Score to display upon death.
    SelectedItemSlot: Annotated[int, 'Range | `0`-`8` | both inclusive'] | None = None  # Hotbar slot the player has selected.
    SelectedItem: SlottedItem[Annotated[int, 'Range | `0`-`8` | both inclusive']] | None = None  # Item in the hotbar slot the player has selected.
    equipment: PlayerEquipment | None = None
    respawn: Respawn | None = None
    SleepTimer: int | None = None  # Ticks the player has been in bed.
    foodLevel: int | None = None  # Level of the hunger bar.
    foodExhaustionLevel: float | None = None  # Rate at which the `foodSaturationLevel` depletes.
    foodSaturationLevel: float | None = None  # Rate at which the hunger bar depletes.
    foodTickTimer: int | None = None  # Ticks until the player heals or takes starvation damage.
    XpLevel: int | None = None  # Number of experience levels the player has.
    XpP: float | None = None  # Percentage the experience bar is filled up.
    XpTotal: int | None = None  # Total experience the player has.
    XpSeed: int | None = None  # Seed for enchantments.
    Inventory: Annotated[list[SlottedItem[PlayerSlot]], 'Length = 0-41 (both inclusive)'] | None = None
    EnderItems: Annotated[list[SlottedItem[Annotated[int, 'Range | `0`-`26` | both inclusive']]], 'Length = 0-27 (both inclusive)'] | None = None  # The player's enderchest inventory.
    abilities: Abilities | None = None  # Abilities of the player.
    entered_nether_pos: tuple[float, float, float] | None = None  # Position that the player entered the nether at.
    raid_omen_position: tuple[int, int, int] | None = None
    RootVehicle: RootVehicle | None = None  # Entity that the player is riding.
    ShoulderEntityLeft: AnyEntity | None = None  # Entity that is on the player's left shoulder.
    ShoulderEntityRight: AnyEntity | None = None  # Entity that is on the player's right shoulder.
    seenCredits: bool | None = None  # Whether the player has gone to the overworld after defeating the Ender Dragon.
    recipeBook: RecipeBook | None = None  # Recipes that the player has.
    warden_spawn_tracker: WardenSpawnTracker | None = None  # Tracking the warden spawning process for this player.
    ender_pearls: list[EnderPearl] | None = None  # Ender pearls thrown by this player.
    post_effects: list[str] | None = None
    last_explosion_impact_pos: tuple[float, float, float] | None = None
    spawn_extra_particles_on_fall: bool | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::player::Player": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::LivingEntity"
                }
            },
            {
                "kind": "pair",
                "desc": "Version of the player NBT structure",
                "key": "DataVersion",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "Dimension",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "reference",
                            "path": "::java::world::entity::mob::player::Dimension",
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.16"
                                        }
                                    }
                                }
                            ]
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
                                            "value": "1.16"
                                        }
                                    }
                                },
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "dimension"
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
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.19"
                            }
                        }
                    }
                ],
                "desc": "Location of the player's last death.",
                "key": "LastDeathLocation",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::GlobalPos"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Game mode that the player is in.",
                "key": "playerGameType",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::player::Gamemode"
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
                "desc": "Previous game mode that the player was in.",
                "key": "previousPlayerGameType",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::player::Gamemode"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Score to display upon death.",
                "key": "Score",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Hotbar slot the player has selected.",
                "key": "SelectedItemSlot",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 8
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Item in the hotbar slot the player has selected.",
                "key": "SelectedItem",
                "type": {
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
                                "value": "1.21.5"
                            }
                        }
                    }
                ],
                "key": "equipment",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::player::PlayerEquipment"
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
                    },
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.5"
                            }
                        }
                    }
                ],
                "desc": "Dimension of the player's respawn point.",
                "key": "SpawnDimension",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "dimension"
                                }
                            }
                        }
                    ]
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
                                "value": "1.16.2"
                            }
                        }
                    },
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.5"
                            }
                        }
                    }
                ],
                "desc": "The Y-rotation of the player's respawn point.",
                "key": "SpawnAngle",
                "type": {
                    "kind": "float"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.5"
                            }
                        }
                    }
                ],
                "desc": "X coordinate of the player's spawn point.",
                "key": "SpawnX",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.5"
                            }
                        }
                    }
                ],
                "desc": "Y coordinate of the player's spawn point.",
                "key": "SpawnY",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.5"
                            }
                        }
                    }
                ],
                "desc": "Z coordinate of the player's spawn point.",
                "key": "SpawnZ",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.5"
                            }
                        }
                    }
                ],
                "desc": "Whether the player must spawn at the spawn point.",
                "key": "SpawnForced",
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
                                "value": "1.21.5"
                            }
                        }
                    }
                ],
                "key": "respawn",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::player::Respawn"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Ticks the player has been in bed.",
                "key": "SleepTimer",
                "type": {
                    "kind": "short"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Level of the hunger bar.",
                "key": "foodLevel",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Rate at which the `foodSaturationLevel` depletes.",
                "key": "foodExhaustionLevel",
                "type": {
                    "kind": "float"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Rate at which the hunger bar depletes.",
                "key": "foodSaturationLevel",
                "type": {
                    "kind": "float"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Ticks until the player heals or takes starvation damage.",
                "key": "foodTickTimer",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Number of experience levels the player has.",
                "key": "XpLevel",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Percentage the experience bar is filled up.",
                "key": "XpP",
                "type": {
                    "kind": "float"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Total experience the player has.",
                "key": "XpTotal",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Seed for enchantments.",
                "key": "XpSeed",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "Inventory",
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
                                "kind": "reference",
                                "path": "::java::world::entity::mob::player::PlayerSlot"
                            }
                        ]
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 41
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "The player's enderchest inventory.",
                "key": "EnderItems",
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
            },
            {
                "kind": "pair",
                "desc": "Abilities of the player.",
                "key": "abilities",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::player::Abilities"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.5"
                            }
                        }
                    }
                ],
                "desc": "Position that the player entered the nether at.",
                "key": "enteredNetherPosition",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::player::EnteredNetherPosition"
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
                                "value": "1.21.5"
                            }
                        }
                    }
                ],
                "desc": "Position that the player entered the nether at.",
                "key": "entered_nether_pos",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "double"
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 3,
                        "max": 3
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
                                "value": "1.20.5"
                            }
                        }
                    }
                ],
                "key": "raid_omen_position",
                "type": {
                    "kind": "int_array",
                    "lengthRange": {
                        "kind": 0,
                        "min": 3,
                        "max": 3
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Entity that the player is riding.",
                "key": "RootVehicle",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::player::RootVehicle"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Entity that is on the player's left shoulder.",
                "key": "ShoulderEntityLeft",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::AnyEntity"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Entity that is on the player's right shoulder.",
                "key": "ShoulderEntityRight",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::AnyEntity"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether the player has gone to the overworld after defeating the Ender Dragon.",
                "key": "seenCredits",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Recipes that the player has.",
                "key": "recipeBook",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::player::RecipeBook"
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
                                "value": "1.19"
                            }
                        }
                    }
                ],
                "desc": "Tracking the warden spawning process for this player.",
                "key": "warden_spawn_tracker",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::player::WardenSpawnTracker"
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
                                "value": "1.21.2"
                            }
                        }
                    }
                ],
                "desc": "Ender pearls thrown by this player.",
                "key": "ender_pearls",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::world::entity::mob::player::EnderPearl"
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
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "key": "post_effects",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "string",
                        "attributes": [
                            {
                                "name": "id",
                                "value": {
                                    "kind": "literal",
                                    "value": {
                                        "kind": "string",
                                        "value": "post_effect"
                                    }
                                }
                            }
                        ]
                    }
                },
                "optional": True
            },
            {
                "kind": "spread",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.20.3"
                            }
                        }
                    },
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.5"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "desc": "Used by the game for wind charges.",
                            "key": "ignore_fall_damage_from_current_explosion",
                            "type": {
                                "kind": "boolean"
                            }
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.5"
                            }
                        }
                    },
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.1"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "desc": "Used by the game for wind charges.",
                            "key": "ignore_fall_damage_from_current_explosion",
                            "type": {
                                "kind": "boolean"
                            },
                            "optional": True
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.1"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::FallDamageLogicData"
                }
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
                                "value": "26.2"
                            }
                        }
                    }
                ],
                "key": "last_explosion_impact_pos",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "double"
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 3,
                        "max": 3
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
                                "value": "1.20.5"
                            }
                        }
                    }
                ],
                "key": "spawn_extra_particles_on_fall",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "CustomName",
                "type": {
                    "kind": "union",
                    "members": []
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "CustomNameVisible",
                "type": {
                    "kind": "union",
                    "members": []
                },
                "optional": True
            }
        ]
    }
}

