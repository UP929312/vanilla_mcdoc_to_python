# Generated from symbols.json for ::java::world::entity::projectile::shulker_bullet::BulletTarget
from dataclasses import dataclass


@dataclass(kw_only=True)
class BulletTarget:
    UUID: tuple[int, int, int, int] | None = None
    X: int | None = None  # X block coordinate of the it.
    Y: int | None = None  # Y block coordinate of the it.
    Z: int | None = None  # Z block coordinate of the it.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::projectile::shulker_bullet::BulletTarget": {
        "kind": "struct",
        "fields": [
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
                "desc": "The upper bits of the its UUID.",
                "key": "M",
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
                "desc": "The lower bits of the its UUID.",
                "key": "L",
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
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "X block coordinate of the it.",
                "key": "X",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Y block coordinate of the it.",
                "key": "Y",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Z block coordinate of the it.",
                "key": "Z",
                "type": {
                    "kind": "int"
                },
                "optional": True
            }
        ]
    }
}

