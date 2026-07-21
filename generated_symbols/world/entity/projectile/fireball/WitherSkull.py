# Generated from symbols.json for ::java::world::entity::projectile::fireball::WitherSkull
from dataclasses import dataclass
from generated_symbols.world.entity.projectile.fireball.DespawnableProjectileBase import DespawnableProjectileBase


@dataclass(kw_only=True)
class WitherSkull(DespawnableProjectileBase):
    dangerous: bool | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::projectile::fireball::WitherSkull": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::projectile::fireball::DespawnableProjectileBase"
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
                                "value": "1.20.3"
                            }
                        }
                    }
                ],
                "key": "dangerous",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

