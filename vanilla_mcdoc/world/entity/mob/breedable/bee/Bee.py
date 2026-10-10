"""
Generated from symbols.json for ::java::world::entity::mob::breedable::bee::Bee
Local link to file: vanilla_mcdoc/world/entity/mob/breedable/bee/Bee.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.minecraft_types import MinecraftUUID
from vanilla_mcdoc.world.entity.mob.NeutralMob import NeutralMob
from vanilla_mcdoc.world.entity.mob.breedable.Breedable import Breedable


class Bee(Breedable, NeutralMob):
    hive_pos: tuple[int, int, int] | None = None
    flower_pos: tuple[int, int, int] | None = None  # Position of the flower the bee is circling
    HasNectar: bool | None = None  # Whether the bee has nectar.
    HasStung: bool | None = None  # Whether the bee has stung an entity.
    TicksSincePollination: int | None = None  # Ticks since the bee has pollinated a crop.
    CannotEnterHiveTicks: int | None = None  # Ticks until the bee can enter its hive.
    CropsGrownSincePollination: int | None = None  # Crops grown since the bee has gathered nectar.
    Anger: int | None = None  # Ticks the bee will be angry for.
    HurtBy: MinecraftUUID | None = None  # Player that has attacked the bee.
