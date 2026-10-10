"""
Generated from symbols.json for ::java::world::entity::mob::breedable::villager::WanderingTrader
Local link to file: vanilla_mcdoc/world/entity/mob/breedable/villager/WanderingTrader.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.world.entity.mob.MobBase import MobBase
from vanilla_mcdoc.world.entity.mob.breedable.villager.VillagerBase import VillagerBase


class WanderingTrader(MobBase, VillagerBase):
    DespawnDelay: int | None = None  # Ticks until it despawns.
    wander_target: tuple[int, int, int] | None = None  # Where it is heading to.
