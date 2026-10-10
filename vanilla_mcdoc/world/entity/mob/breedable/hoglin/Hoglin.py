"""
Generated from symbols.json for ::java::world::entity::mob::breedable::hoglin::Hoglin
Local link to file: vanilla_mcdoc/world/entity/mob/breedable/hoglin/Hoglin.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.world.entity.mob.breedable.Breedable import Breedable


class Hoglin(Breedable):
    IsImmuneToZombification: bool | None = None  # Whether it will not transform to a zoglin when it is in the Overword.
    CannotBeHunted: bool | None = None  # Whether it cannot be hunted by piglins
    TimeInOverworld: int | None = None  # The number of ticks it has been in the overworld.
