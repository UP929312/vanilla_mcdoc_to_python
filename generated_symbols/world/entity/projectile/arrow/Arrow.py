# Generated from symbols.json for ::java::world::entity::projectile::arrow::Arrow
from dataclasses import dataclass
from generated_symbols.world.entity.projectile.arrow.ArrowBase import ArrowBase


@dataclass(kw_only=True)
class Arrow(ArrowBase):
    pass


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::projectile::arrow::Arrow": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::projectile::arrow::ArrowBase"
                }
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
                "desc": "Color of the arrow's potion bubble trail particles.\ncalculated as `RED << 16 | GREEN << 8 | BLUE`. Each of these fields must be between 0 and 255, inclusive.",
                "key": "Color",
                "type": {
                    "kind": "int",
                    "attributes": [
                        {
                            "name": "color",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "composite_rgb"
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
                "desc": "Effects to give to the hit entity.",
                "key": "CustomPotionEffects",
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
                "desc": "Effects to give to the hit entity.",
                "key": "custom_potion_effects",
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
                                "value": "1.20.5"
                            }
                        }
                    }
                ],
                "desc": "Name of the default potion effect.",
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
                                    "value": "mob_effect"
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

