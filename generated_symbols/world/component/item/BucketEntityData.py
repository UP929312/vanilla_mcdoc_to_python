# Generated from symbols.json for ::java::world::component::item::BucketEntityData
from dataclasses import dataclass


@dataclass(kw_only=True)
class BucketEntityData:
    NoAI: bool | None = None  # Whether it should have an AI.
    Silent: bool | None = None  # Whether the entity should make any sound.
    NoGravity: bool | None = None  # Whether the entity should be effected by gravity.
    Glowing: bool | None = None  # Whether the entity should glow.
    Invulnerable: bool | None = None  # Whether the entity should take damage.
    PersistenceRequired: bool | None = None  # Whether the entity should not despawn naturally.
    Health: float | None = None
    HuntingCooldown: int | None = None  # Turns into the expiry time of the memory module `has_hunting_cooldown` for axolotls.
    Age: int | None = None  # The age for axolotl and tadpole.
    AgeLocked: bool | None = None  # The age locked state for axolotl and tadpole.
    age: int | None = None  # The age for sulfur cube.
    age_locked: bool | None = None  # The age locked state for sulfur cube.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::BucketEntityData": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Whether it should have an AI.",
                "key": "NoAI",
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
                "desc": "Whether the entity should be effected by gravity.",
                "key": "NoGravity",
                "type": {
                    "kind": "boolean"
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
                "desc": "Whether the entity should take damage.",
                "key": "Invulnerable",
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
                                "value": "26.2"
                            }
                        }
                    }
                ],
                "desc": "Whether the entity should not despawn naturally.",
                "key": "PersistenceRequired",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
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
                "desc": "Turns into the expiry time of the memory module `has_hunting_cooldown` for axolotls.",
                "key": "HuntingCooldown",
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
                                "value": "1.21.4"
                            }
                        }
                    }
                ],
                "desc": "Turns into the `Variant` entity tag for tropical fish.",
                "key": "BucketVariantTag",
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
                                "value": "1.21.4"
                            }
                        }
                    }
                ],
                "desc": "The variant for axolotl.",
                "key": "Variant",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::breedable::axolotl::AxolotlVariantInt"
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
                                "value": "1.21.4"
                            }
                        }
                    }
                ],
                "desc": "The size variant for salmon.",
                "key": "type",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::entity::SalmonType"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "The age for axolotl and tadpole.",
                "key": "Age",
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
                                "value": "26.1"
                            }
                        }
                    }
                ],
                "desc": "The age locked state for axolotl and tadpole.",
                "key": "AgeLocked",
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
                                "value": "26.2"
                            }
                        }
                    }
                ],
                "desc": "The age for sulfur cube.",
                "key": "age",
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
                                "value": "26.2"
                            }
                        }
                    }
                ],
                "desc": "The age locked state for sulfur cube.",
                "key": "age_locked",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

