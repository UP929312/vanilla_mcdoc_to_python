"""
Generated from symbols.json for ::java::world::entity::projectile::firework_rocket::FireWorkRocket
Local link to file: vanilla_mcdoc/world/entity/projectile/firework_rocket/FireWorkRocket.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.world.entity.projectile.ProjectileBase import ProjectileBase

if TYPE_CHECKING:
    from vanilla_mcdoc.world.item.ItemStack import ItemStack


class FireWorkRocket(ProjectileBase):
    Life: int | None = None  # Ticks it has existed.
    LifeTime: int | None = None  # Ticks it will exist.
    ShotAtAngle: bool | None = None  # Whether it should move at an angle.
    FireworksItem: ItemStack | None = None
