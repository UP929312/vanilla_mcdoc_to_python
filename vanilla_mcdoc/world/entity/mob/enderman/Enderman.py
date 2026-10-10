"""
Generated from symbols.json for ::java::world::entity::mob::enderman::Enderman
Local link to file: vanilla_mcdoc/world/entity/mob/enderman/Enderman.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.world.entity.mob.MobBase import MobBase
from vanilla_mcdoc.world.entity.mob.NeutralMob import NeutralMob

if TYPE_CHECKING:
    from vanilla_mcdoc.util.BlockState import BlockState


class Enderman(MobBase, NeutralMob):
    carriedBlockState: BlockState | None = None  # Block it is carrying.
