"""
Generated from symbols.json for ::java::world::entity::projectile::ProjectileBase
Local link to file: vanilla_mcdoc/world/entity/projectile/ProjectileBase.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.minecraft_types import MinecraftUUID
from vanilla_mcdoc.world.entity.EntityBase import EntityBase

if TYPE_CHECKING:
    from vanilla_mcdoc.world.component.item.AdventureModePredicate import AdventureModePredicate


class ProjectileBase(EntityBase):
    HasBeenShot: bool | None = None  # Whether it has been shot. This is set to true when it exists for at least one tick, and is used by the game to ensure it only triggers the projectile_shoot game event once.
    Owner: MinecraftUUID | None = None
    LeftOwner: bool | None = None  # Whether it has left its owner.
    can_break: AdventureModePredicate | None = None
