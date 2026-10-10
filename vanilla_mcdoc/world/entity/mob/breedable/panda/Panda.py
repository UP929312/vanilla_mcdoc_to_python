"""
Generated from symbols.json for ::java::world::entity::mob::breedable::panda::Panda
Local link to file: vanilla_mcdoc/world/entity/mob/breedable/panda/Panda.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.world.entity.mob.breedable.Breedable import Breedable

if TYPE_CHECKING:
    from vanilla_mcdoc.world.entity.mob.breedable.panda.Gene import Gene


class Panda(Breedable):
    MainGene: Gene | None = None  # Displayed gene. If this gene is recessive and 'HiddenGene' is not the same, the panda will display the 'normal' gene.
    HiddenGene: Gene | None = None  # Hidden gene.
