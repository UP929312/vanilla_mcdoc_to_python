# Generated from symbols.json for ::java::world::entity::projectile::fireball::DespawnableProjectileBase
from dataclasses import dataclass
from generated_symbols.world.entity.projectile.fireball.AcceleratingProjectileBase import AcceleratingProjectileBase


@dataclass(kw_only=True)
class DespawnableProjectileBase(AcceleratingProjectileBase):
    pass


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::projectile::fireball::DespawnableProjectileBase": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::projectile::fireball::AcceleratingProjectileBase"
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
                                "value": "1.16"
                            }
                        }
                    }
                ],
                "key": "direction",
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
                "desc": "Ticks since it last moved.",
                "key": "life",
                "type": {
                    "kind": "short"
                },
                "optional": True
            }
        ]
    }
}

