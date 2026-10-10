"""
Generated from symbols.json for ::java::world::entity::mob::breedable::horse::Llama
Local link to file: vanilla_mcdoc/world/entity/mob/breedable/horse/Llama.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.world.entity.mob.breedable.horse.ChestedHorse import ChestedHorse

if TYPE_CHECKING:
    from vanilla_mcdoc.world.entity.mob.breedable.horse.LlamaVariantInt import LlamaVariantInt


class Llama(ChestedHorse):
    Strength: Annotated[int, Field(ge=1, le=5)] | None = None  # Determines both the number of items it can carry and how likely it is for wolves to run away.
    Variant: LlamaVariantInt | None = None  # The variant of this llama.
