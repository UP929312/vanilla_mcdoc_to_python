"""
Generated from symbols.json for ::java::world::entity::projectile::fireball::LargeFireball
Local link to file: vanilla_mcdoc/world/entity/projectile/fireball/LargeFireball.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.world.entity.projectile.fireball.FireballBase import FireballBase


class LargeFireball(FireballBase):
    ExplosionPower: int | None = None  # Explosion radius.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::projectile::fireball::LargeFireball": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::projectile::fireball::FireballBase"
                }
            },
            {
                "kind": "pair",
                "desc": "Explosion radius.",
                "key": "ExplosionPower",
                "type": {
                    "kind": "int"
                },
                "optional": True
            }
        ]
    }
}
