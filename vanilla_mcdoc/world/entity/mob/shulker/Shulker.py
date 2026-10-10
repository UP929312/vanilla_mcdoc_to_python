"""
Generated from symbols.json for ::java::world::entity::mob::shulker::Shulker
Local link to file: vanilla_mcdoc/world/entity/mob/shulker/Shulker.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.world.entity.mob.MobBase import MobBase

if TYPE_CHECKING:
    from vanilla_mcdoc.util.color.DyeColorByte import DyeColorByte
    from vanilla_mcdoc.util.direction.DirectionByte import DirectionByte
    from vanilla_mcdoc.world.entity.mob.shulker.ShulkerColor import ShulkerColor


class Shulker(MobBase):
    Peek: bool | None = None  # Whether it is peeking.
    AttachFace: DirectionByte | None = None  # Which face it is attached to.
    Color: DyeColorByte | ShulkerColor | None = None
