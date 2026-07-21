# Generated from symbols.json for ::java::world::entity::mob::LivingEntity
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Any
from generated_symbols.world.entity.EntityBase import EntityBase
from generated_symbols.world.entity.mob.FallDamageLogicData import FallDamageLogicData

if TYPE_CHECKING:
    from generated_symbols.util.effect.MobEffectInstance import MobEffectInstance
    from generated_symbols.world.entity.mob.Attribute import Attribute
    from generated_symbols.world.entity.mob.WaypointIcon import WaypointIcon


@dataclass(kw_only=True)
class LivingEntity(EntityBase, FallDamageLogicData):
    Health: float | None = None
    AbsorptionAmount: float | None = None  # How much absorption health it has.
    HurtTime: int | None = None  # Timer since it has been damaged. Counts down to zero.
    DeathTime: int | None = None  # Timer since it was marked as dead. Counts down to zero.
    FallFlying: bool | None = None  # Whether it will glide when it falls.
    sleeping_pos: tuple[int, int, int] | None = None
    Brain: Any | None = None
    attributes: list[Attribute] | None = None
    active_effects: list[MobEffectInstance] | None = None
    last_hurt_by_player: tuple[int, int, int, int] | None = None  # The UUID of the player that last hurt this entity. Stored for 100 ticks.
    last_hurt_by_player_memory_time: Annotated[int, 'Range | `0`-`100` | both inclusive'] | None = None  # Amount of ticks that this entity will remember the player that last hurt this entity. Counts down from 100 to 0.
    last_hurt_by_mob: tuple[int, int, int, int] | None = None  # The UUID of the mob that last hurt this entity. Stored for 100 ticks.
    ticks_since_last_hurt_by_mob: Annotated[int, 'Range | `0`-`100` | both inclusive'] | None = None  # Amount of ticks since this entity was last hurt by a mob. Counts up from 0 to 100.
    locator_bar_icon: WaypointIcon | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::LivingEntity": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::EntityBase"
                }
            },
            {
                "kind": "pair",
                "key": "Health",
                "type": {
                    "kind": "float"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "How much absorption health it has.",
                "key": "AbsorptionAmount",
                "type": {
                    "kind": "float"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Timer since it has been damaged. Counts down to zero.",
                "key": "HurtTime",
                "type": {
                    "kind": "short"
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
                                "value": "26.2"
                            }
                        }
                    }
                ],
                "desc": "Ticks since it was last damaged, from its creation.",
                "key": "HurtByTimestamp",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Timer since it was marked as dead. Counts down to zero.",
                "key": "DeathTime",
                "type": {
                    "kind": "short"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether it will glide when it falls.",
                "key": "FallFlying",
                "type": {
                    "kind": "boolean"
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
                "desc": "X coordinate of where it is sleeping.",
                "key": "SleepingX",
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
                "desc": "Y coordinate of where it is sleeping.",
                "key": "SleepingY",
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
                "desc": "Z coordinate of where it is sleeping.",
                "key": "SleepingZ",
                "type": {
                    "kind": "int"
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
                "key": "sleeping_pos",
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
                "key": "Brain",
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "memories",
                            "type": {
                                "kind": "reference",
                                "path": "::java::util::memory::Memories"
                            },
                            "optional": True
                        }
                    ]
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
                                "value": "1.21"
                            }
                        }
                    }
                ],
                "key": "Attributes",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::world::entity::mob::Attribute"
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
                                "value": "1.21"
                            }
                        }
                    }
                ],
                "key": "attributes",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::world::entity::mob::Attribute"
                    }
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
                                "value": "1.20.2"
                            }
                        }
                    }
                ],
                "desc": "Active potion effects",
                "key": "ActiveEffects",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::util::effect::MobEffectInstance"
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
                                "value": "1.20.2"
                            }
                        }
                    }
                ],
                "key": "active_effects",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::util::effect::MobEffectInstance"
                    }
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
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "desc": "Team to join when it is spawned.",
                "key": "Team",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "team"
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
                                "value": "1.21.4"
                            }
                        }
                    }
                ],
                "desc": "The UUID of the player that last hurt this entity. Stored for 100 ticks.",
                "key": "last_hurt_by_player",
                "type": {
                    "kind": "int_array",
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
                                "value": "1.21.4"
                            }
                        }
                    }
                ],
                "desc": "Amount of ticks that this entity will remember the player that last hurt this entity.\nCounts down from 100 to 0.",
                "key": "last_hurt_by_player_memory_time",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 100
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
                                "value": "1.21.4"
                            }
                        }
                    }
                ],
                "desc": "The UUID of the mob that last hurt this entity. Stored for 100 ticks.",
                "key": "last_hurt_by_mob",
                "type": {
                    "kind": "int_array",
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
                                "value": "1.21.4"
                            }
                        }
                    }
                ],
                "desc": "Amount of ticks since this entity was last hurt by a mob.\nCounts up from 0 to 100.",
                "key": "ticks_since_last_hurt_by_mob",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 100
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
                                "value": "1.21.6"
                            }
                        }
                    }
                ],
                "key": "locator_bar_icon",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::WaypointIcon"
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
                                "value": "26.1"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::FallDamageLogicData"
                }
            }
        ]
    }
}

