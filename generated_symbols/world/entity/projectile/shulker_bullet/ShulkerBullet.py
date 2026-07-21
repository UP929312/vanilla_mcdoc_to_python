# Generated from symbols.json for ::java::world::entity::projectile::shulker_bullet::ShulkerBullet
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.entity.projectile.ProjectileBase import ProjectileBase

if TYPE_CHECKING:
    from generated_symbols.util.direction.DirectionByte import DirectionByte
    from generated_symbols.world.entity.projectile.shulker_bullet.BulletTarget import BulletTarget


@dataclass(kw_only=True)
class ShulkerBullet(ProjectileBase):
    Steps: int | None = None  # Steps it takes to reach the target
    Target: BulletTarget | None = None
    Dir: DirectionByte | None = None
    TXD: float | None = None  # X offset to move based on the target's location.
    TYD: float | None = None  # Y offset to move based on the target's location.
    TZD: float | None = None  # Z offset to move based on the target's location.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::projectile::shulker_bullet::ShulkerBullet": {
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
                                "value": "1.16"
                            }
                        }
                    }
                ],
                "key": "Owner",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::projectile::shulker_bullet::BulletTarget"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Steps it takes to reach the target",
                "key": "Steps",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "Target",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::projectile::shulker_bullet::BulletTarget"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "Dir",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::direction::DirectionByte"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "X offset to move based on the target's location.",
                "key": "TXD",
                "type": {
                    "kind": "double"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Y offset to move based on the target's location.",
                "key": "TYD",
                "type": {
                    "kind": "double"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Z offset to move based on the target's location.",
                "key": "TZD",
                "type": {
                    "kind": "double"
                },
                "optional": True
            }
        ]
    }
}

