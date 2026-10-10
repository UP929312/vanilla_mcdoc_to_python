"""
Generated from symbols.json for ::java::world::entity::mob::breedable::tamable::Tamable
Local link to file: vanilla_mcdoc/world/entity/mob/breedable/tamable/Tamable.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.minecraft_types import MinecraftUUID
from vanilla_mcdoc.world.entity.mob.breedable.Breedable import Breedable


class Tamable(Breedable):
    Owner: MinecraftUUID | None = None
    Sitting: bool | None = None  # Whether the mob is sitting.
