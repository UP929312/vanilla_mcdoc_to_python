"""
Generated from symbols.json for ::java::world::entity::mob::breedable::tamable::Wolf
Local link to file: vanilla_mcdoc/world/entity/mob/breedable/tamable/Wolf.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.minecraft_types import IdSpec
from vanilla_mcdoc.world.entity.mob.NeutralMob import NeutralMob
from vanilla_mcdoc.world.entity.mob.breedable.tamable.Tamable import Tamable

if TYPE_CHECKING:
    from vanilla_mcdoc.util.DyeColorByte import DyeColorByte


class Wolf(NeutralMob, Tamable):
    CollarColor: DyeColorByte | None = None  # Collar color, present for wild wolfs. Defaults to 14 (red).
    variant: Annotated[str, IdSpec(registry='wolf_variant')] | None = None
    sound_variant: Annotated[str, IdSpec(registry='wolf_sound_variant')] | None = None
