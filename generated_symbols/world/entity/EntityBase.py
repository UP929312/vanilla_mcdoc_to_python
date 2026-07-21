# Generated from symbols.json for ::java::world::entity::EntityBase
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.text.Text import Text
    from generated_symbols.world.component.CustomData import CustomData
    from generated_symbols.world.entity.AnyEntity import AnyEntity


@dataclass(kw_only=True)
class EntityBase:
    Pos: tuple[float, float, float] | None = None
    Motion: tuple[float, float, float] | None = None
    Rotation: tuple[float, float] | None = None  # Rotation in [y-rotation, x-rotation]
    fall_distance: float | None = None  # How far the entity has fallen.
    Fire: int | None = None  # Ticks of fire left, or if negative, ticks until the entity starts to burn.
    Air: int | None = None  # Ticks of air left.
    HasVisualFire: bool | None = None  # Whether the entity has visual fire.
    OnGround: bool | None = None  # Whether the entity is on the ground.
    NoGravity: bool | None = None  # Whether the entity should be effected by gravity.
    Invulnerable: bool | None = None  # Whether the entity should take damage.
    PortalCooldown: int | None = None  # How long until the entity can go through a nether portal.
    UUID: tuple[int, int, int, int] | None = None
    CustomName: Text | None = None
    CustomNameVisible: bool | None = None  # Whether the custom name should always be visible.
    Silent: bool | None = None  # Whether the entity should make any sound.
    Passengers: list[AnyEntity] | None = None  # Passengers on the entity.
    Glowing: bool | None = None  # Whether the entity should glow.
    Tags: list[str] | None = None  # Labelling tags on the entity.
    Team: str | None = None  # Team to join when it is spawned.
    data: CustomData | None = None  # Any stored data
    TicksFrozen: int | None = None  # Ticks that this entity has been freezing. Although this tag is defined for all entities, it is actually only used by mobs that are not in the `freeze_immune_entity_types` entity type tag. This increases by one every tick the entity is in powdered snow, and decreases by two when it's out of it.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::EntityBase": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "Pos",
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
                "key": "Motion",
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
                "desc": "Rotation in [y-rotation, x-rotation]",
                "key": "Rotation",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "float"
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 2,
                        "max": 2
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
                                "value": "1.21.5"
                            }
                        }
                    }
                ],
                "desc": "How far the entity has fallen.",
                "key": "FallDistance",
                "type": {
                    "kind": "float"
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
                "desc": "How far the entity has fallen.",
                "key": "fall_distance",
                "type": {
                    "kind": "double"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Ticks of fire left, or if negative, ticks until the entity starts to burn.",
                "key": "Fire",
                "type": {
                    "kind": "short"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Ticks of air left.",
                "key": "Air",
                "type": {
                    "kind": "short"
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
                                "value": "1.17"
                            }
                        }
                    }
                ],
                "desc": "Whether the entity has visual fire.",
                "key": "HasVisualFire",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether the entity is on the ground.",
                "key": "OnGround",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether the entity should be effected by gravity.",
                "key": "NoGravity",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether the entity should take damage.",
                "key": "Invulnerable",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "How long until the entity can go through a nether portal.",
                "key": "PortalCooldown",
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
                "desc": "Upper bits of the entity's UUID.",
                "key": "UUIDMost",
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
                "desc": "Lower bits of the entity's UUID.",
                "key": "UUIDLeast",
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
                "key": "UUID",
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
                "key": "CustomName",
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
                                            "value": "1.21.5"
                                        }
                                    }
                                },
                                {
                                    "name": "text_component"
                                }
                            ]
                        },
                        {
                            "kind": "reference",
                            "path": "::java::util::text::Text",
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
                            ]
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether the custom name should always be visible.",
                "key": "CustomNameVisible",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether the entity should make any sound.",
                "key": "Silent",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Passengers on the entity.",
                "key": "Passengers",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::world::entity::AnyEntity"
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether the entity should glow.",
                "key": "Glowing",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Labelling tags on the entity.",
                "key": "Tags",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "string",
                        "attributes": [
                            {
                                "name": "tag"
                            }
                        ]
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
                                "value": "1.21.5"
                            }
                        }
                    }
                ],
                "desc": "Any stored data",
                "key": "data",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::CustomData"
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
                                "value": "1.17"
                            }
                        }
                    }
                ],
                "desc": "Ticks that this entity has been freezing. Although this tag is defined for all entities,\nit is actually only used by mobs that are not in the `freeze_immune_entity_types` entity type tag.\nThis increases by one every tick the entity is in powdered snow, and decreases by two when it's out of it.",
                "key": "TicksFrozen",
                "type": {
                    "kind": "int"
                },
                "optional": True
            }
        ]
    }
}

