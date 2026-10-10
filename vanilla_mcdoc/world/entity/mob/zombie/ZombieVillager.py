"""
Generated from symbols.json for ::java::world::entity::mob::zombie::ZombieVillager
Local link to file: vanilla_mcdoc/world/entity/mob/zombie/ZombieVillager.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from pydantic import Field

from vanilla_mcdoc.minecraft_types import MinecraftUUID
from vanilla_mcdoc.world.entity.mob.zombie.Zombie import Zombie

if TYPE_CHECKING:
    from vanilla_mcdoc.world.entity.mob.breedable.villager.Offers import Offers
    from vanilla_mcdoc.world.entity.mob.breedable.villager.PlayerReputationPart import PlayerReputationPart
    from vanilla_mcdoc.world.entity.mob.breedable.villager.VillagerData import VillagerData


class ZombieVillager(Zombie):
    VillagerData_: VillagerData | None = Field(default=None, alias='VillagerData')  # Villager's skin data
    VillagerDataFinalized: bool | None = None
    Gossips: list[PlayerReputationPart] | None = None  # Villager's gossips
    Offers_: Offers | None = Field(default=None, alias='Offers')  # Villager's offers
    ConversionTime: int | None = None  # Ticks until the it is converted.
    ConversionPlayer: MinecraftUUID | None = None  # Player who triggered the conversion.
