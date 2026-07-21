# Generated from symbols.json for ::java::world::entity::area_effect_cloud::AreaEffectCloud
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any
from generated_symbols.world.entity.EntityBase import EntityBase

if TYPE_CHECKING:
    from generated_symbols.util.particle.Particle import Particle


@dataclass(kw_only=True)
class AreaEffectCloud(EntityBase):
    Age: int | None = None  # Number of ticks it has existed. Controls when it will despawn; when greater than `Duration + WaitTime`.
    Color: int | None = None  # Color of the particles. calculated as `RED << 16 | GREEN << 8 | BLUE`. Each of these fields must be between 0 and 255, inclusive
    Duration: int | None = None  # Maximum number of ticks until it will disappear after `WaitTime` is done
    ReapplicationDelay: int | None = None  # Number of ticks until the effects are reapplied.
    WaitTime: int | None = None  # Number of ticks until it appears.
    DurationOnUse: int | None = None  # Amount the duration changes when it is active.
    Owner: tuple[int, int, int, int] | None = None
    Radius: float | None = None  # Radius of the particles & effect applications.
    RadiusOnUse: float | None = None  # Change in the radius when it is used.
    RadiusPerTick: float | None = None  # Change in the radius per tick.
    custom_particle: Particle | None = None  # If present, the particle that the area effect cloud displays instead of the default `entity_effect` particle based on the potion contents.
    potion_contents: Any | None = None
    potion_duration_scale: float | None = None  # The duration of the potion effect applied is scaled by this factor. Defaults to `1`. Will be `0.25` when throwing lingering potions.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::area_effect_cloud::AreaEffectCloud": {
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
                "desc": "Number of ticks it has existed.\nControls when it will despawn; when greater than `Duration + WaitTime`.",
                "key": "Age",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Color of the particles.\ncalculated as `RED << 16 | GREEN << 8 | BLUE`. Each of these fields must be between 0 and 255, inclusive",
                "key": "Color",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Maximum number of ticks until it will disappear after `WaitTime` is done",
                "key": "Duration",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Number of ticks until the effects are reapplied.",
                "key": "ReapplicationDelay",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Number of ticks until it appears.",
                "key": "WaitTime",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Amount the duration changes when it is active.",
                "key": "DurationOnUse",
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
                                "value": "1.16"
                            }
                        }
                    }
                ],
                "desc": "Upper bits of the owner's UUID.",
                "key": "OwnerUUIDMost",
                "type": {
                    "kind": "long"
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
                                "value": "1.16"
                            }
                        }
                    }
                ],
                "desc": "Lower bits of the owner's UUID.",
                "key": "OwnerUUIDLeast",
                "type": {
                    "kind": "long"
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
                "key": "Owner",
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
                "desc": "Radius of the particles & effect applications.",
                "key": "Radius",
                "type": {
                    "kind": "float"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Change in the radius when it is used.",
                "key": "RadiusOnUse",
                "type": {
                    "kind": "float"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Change in the radius per tick.",
                "key": "RadiusPerTick",
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
                                "value": "1.21.6"
                            }
                        }
                    }
                ],
                "desc": "Particle the area effect cloud displays.",
                "key": "Particle",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.20.5"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "reference",
                            "path": "::java::util::particle::Particle",
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
                                "value": "1.21.6"
                            }
                        }
                    }
                ],
                "desc": "If present, the particle that the area effect cloud displays instead of the default `entity_effect` particle based on the potion contents.",
                "key": "custom_particle",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::particle::Particle"
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
                                "value": "1.20.5"
                            }
                        }
                    }
                ],
                "desc": "Default potion effect.",
                "key": "Potion",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "potion"
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
                "desc": "Potion effects that get applied on use.",
                "key": "Effects",
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
                    },
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.20.5"
                            }
                        }
                    }
                ],
                "desc": "Potion effects that get applied on use.",
                "key": "effects",
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
                                "value": "1.20.5"
                            }
                        }
                    }
                ],
                "key": "potion_contents",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "static",
                            "value": "potion_contents"
                        }
                    ],
                    "registry": "minecraft:data_component"
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
                "desc": "The duration of the potion effect applied is scaled by this factor. Defaults to `1`.\nWill be `0.25` when throwing lingering potions.",
                "key": "potion_duration_scale",
                "type": {
                    "kind": "float"
                },
                "optional": True
            }
        ]
    }
}

