"""
Generated from symbols.json for ::java::world::entity::mob::breedable::armadillo::Armadillo
Local link to file: vanilla_mcdoc/world/entity/mob/breedable/armadillo/Armadillo.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.world.entity.mob.breedable.Breedable import Breedable

if TYPE_CHECKING:
    from vanilla_mcdoc.world.entity.mob.breedable.armadillo.ArmadilloState import ArmadilloState


class Armadillo(Breedable):
    state: ArmadilloState | None = None
    scute_time: Annotated[int, Field(ge=0)] | None = None
