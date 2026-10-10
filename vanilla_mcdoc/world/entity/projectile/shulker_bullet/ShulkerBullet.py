"""
Generated from symbols.json for ::java::world::entity::projectile::shulker_bullet::ShulkerBullet
Local link to file: vanilla_mcdoc/world/entity/projectile/shulker_bullet/ShulkerBullet.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.world.entity.projectile.ProjectileBase import ProjectileBase

if TYPE_CHECKING:
    from vanilla_mcdoc.util.direction.DirectionByte import DirectionByte
    from vanilla_mcdoc.world.entity.projectile.shulker_bullet.BulletTarget import BulletTarget


class ShulkerBullet(ProjectileBase):
    Steps: int | None = None  # Steps it takes to reach the target
    Target: BulletTarget | None = None
    Dir: DirectionByte | None = None
    TXD: float | None = None  # X offset to move based on the target's location.
    TYD: float | None = None  # Y offset to move based on the target's location.
    TZD: float | None = None  # Z offset to move based on the target's location.
