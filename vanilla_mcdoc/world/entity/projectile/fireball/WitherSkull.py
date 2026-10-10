"""
Generated from symbols.json for ::java::world::entity::projectile::fireball::WitherSkull
Local link to file: vanilla_mcdoc/world/entity/projectile/fireball/WitherSkull.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.world.entity.projectile.fireball.DespawnableProjectileBase import DespawnableProjectileBase


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
