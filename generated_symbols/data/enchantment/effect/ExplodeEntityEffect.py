# Generated from symbols.json for ::java::data::enchantment::effect::ExplodeEntityEffect
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.LevelBasedValue import LevelBasedValue
    from generated_symbols.data.enchantment.effect.BlockInteraction import BlockInteraction
    from generated_symbols.data.enchantment.effect.ExplosionParticleInfo import ExplosionParticleInfo
    from generated_symbols.data.util.SoundEventRef import SoundEventRef
    from generated_symbols.util.particle.Particle import Particle


@dataclass(kw_only=True)
class ExplodeEntityEffect:
    radius: LevelBasedValue
    block_interaction: BlockInteraction  # Whether the explosion has special effects on blocks.
    small_particle: Particle
    large_particle: Particle
    sound: SoundEventRef
    attribute_to_user: bool | None = None  # Whether the explosion should be attributed to the user of the enchanted tool.
    damage_type: str | None = None  # If omitted, no damage is dealt by the explosion.
    immune_blocks: str | list[str] | None = None  # List of Blocks or hash-prefixed Block Tag specifying which blocks fully block the explosion.
    knockback_multiplier: LevelBasedValue | None = None  # If omitted, constant value `1` is applied.
    offset: tuple[float, float, float] | None = None  # Relative coordinates to offset the explosion by. Defaults to `[0, 0, 0]`.
    create_fire: bool | None = None  # Whether fire is placed within the explosion radius.
    block_particles: list[ExplosionParticleInfo] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect::ExplodeEntityEffect": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Whether the explosion should be attributed to the user of the enchanted tool.",
                "key": "attribute_to_user",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "If omitted, no damage is dealt by the explosion.",
                "key": "damage_type",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "damage_type"
                                }
                            }
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "List of Blocks or hash-prefixed Block Tag specifying which blocks fully block the explosion.",
                "key": "immune_blocks",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "tree",
                                        "values": {
                                            "registry": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "block"
                                                }
                                            },
                                            "tags": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "allowed"
                                                }
                                            }
                                        }
                                    }
                                }
                            ]
                        },
                        {
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
                                                "value": "block"
                                            }
                                        }
                                    }
                                ]
                            }
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "If omitted, constant value `1` is applied.",
                "key": "knockback_multiplier",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::LevelBasedValue"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Relative coordinates to offset the explosion by. Defaults to `[0, 0, 0]`.",
                "key": "offset",
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
                "key": "radius",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::LevelBasedValue"
                }
            },
            {
                "kind": "pair",
                "desc": "Whether fire is placed within the explosion radius.",
                "key": "create_fire",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether the explosion has special effects on blocks.",
                "key": "block_interaction",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::effect::BlockInteraction"
                }
            },
            {
                "kind": "pair",
                "key": "small_particle",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::particle::Particle"
                }
            },
            {
                "kind": "pair",
                "key": "large_particle",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::particle::Particle"
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
                                "value": "1.21.9"
                            }
                        }
                    }
                ],
                "key": "block_particles",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::enchantment::effect::ExplosionParticleInfo"
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "sound",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::util::SoundEventRef"
                }
            }
        ]
    }
}

