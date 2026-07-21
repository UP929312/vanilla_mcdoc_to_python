# Generated from symbols.json for ::java::world::entity::projectile::arrow::ArrowBase
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.entity.projectile.ProjectileBase import ProjectileBase

if TYPE_CHECKING:
    from generated_symbols.util.block_state.BlockState import BlockState
    from generated_symbols.world.entity.projectile.arrow.Pickup import Pickup
    from generated_symbols.world.item.ItemStack import ItemStack


@dataclass(kw_only=True)
class ArrowBase(ProjectileBase):
    shake: int | None = None  # Shake it creates.
    pickup: Pickup | None = None  # How players can pick up it.
    life: int | None = None  # Ticks since it last moved.
    damage: float | None = None  # Damage it should deal.
    inGround: bool | None = None  # Whether it is in the ground.
    inBlockState: BlockState | None = None  # Block it is in.
    crit: bool | None = None  # Whether it should do critical damage.
    weapon: ItemStack | None = None  # The item which has shot this arrow.
    PierceLevel: int | None = None  # Number of entities it can pass through.
    SoundEvent: str | None = None  # Sound event to play when it hits something.  Can only be vanilla sound events
    item: ItemStack | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::projectile::arrow::ArrowBase": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::projectile::ProjectileBase"
                }
            },
            {
                "kind": "pair",
                "desc": "Shake it creates.",
                "key": "shake",
                "type": {
                    "kind": "byte"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "How players can pick up it.",
                "key": "pickup",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::projectile::arrow::Pickup"
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
                "desc": "Whether a player shot it.",
                "key": "player",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Ticks since it last moved.",
                "key": "life",
                "type": {
                    "kind": "short"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Damage it should deal.",
                "key": "damage",
                "type": {
                    "kind": "double"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether it is in the ground.",
                "key": "inGround",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Block it is in.",
                "key": "inBlockState",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::block_state::BlockState"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether it should do critical damage.",
                "key": "crit",
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
                                "value": "1.21"
                            }
                        }
                    }
                ],
                "desc": "Whether it was shot from a crossbow.",
                "key": "ShotFromCrossbow",
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
                                "value": "1.21"
                            }
                        }
                    }
                ],
                "desc": "The item which has shot this arrow.",
                "key": "weapon",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::item::ItemStack"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Number of entities it can pass through.",
                "key": "PierceLevel",
                "type": {
                    "kind": "byte"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Sound event to play when it hits something.\n\nCan only be vanilla sound events",
                "key": "SoundEvent",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "sound_event"
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
                                "value": "1.20.3"
                            }
                        }
                    }
                ],
                "key": "item",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::item::ItemStack"
                },
                "optional": True
            }
        ]
    }
}

