# Generated from symbols.json for ::java::world::entity::projectile::fireball::AcceleratingProjectileBase
from dataclasses import dataclass
from generated_symbols.world.entity.projectile.ProjectileBase import ProjectileBase


@dataclass(kw_only=True)
class AcceleratingProjectileBase(ProjectileBase):
    acceleration_power: float | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::projectile::fireball::AcceleratingProjectileBase": {
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
                "desc": "Acceleration",
                "key": "power",
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
                                "value": "1.21"
                            }
                        }
                    }
                ],
                "key": "acceleration_power",
                "type": {
                    "kind": "double"
                },
                "optional": True
            }
        ]
    }
}

