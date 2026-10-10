"""
Generated from symbols.json for ::java::world::entity::minecart::SpawnerMinecart
Local link to file: vanilla_mcdoc/world/entity/minecart/SpawnerMinecart.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.world.entity.minecart.Minecart import Minecart

if TYPE_CHECKING:
    from vanilla_mcdoc.world.block.spawner.SpawnPotential import SpawnPotential
    from vanilla_mcdoc.world.block.spawner.SpawnerEntry import SpawnerEntry


class SpawnerMinecart(Minecart):
    SpawnPotentials: list[SpawnPotential] | None = None  # List of potential entities to place next.
    SpawnData: SpawnerEntry | None = None  # Data for the next mob to place. Will be overwritten by `SpawnPotentials`.
    SpawnCount: int  # Number of entities that will be placed.
    SpawnRange: int | None = None  # Range that the spawned entities will be placed in.
    Delay: int | None = None  # Ticks until the next spawn.
    MinSpawnDelay: int | None = None  # Minimum random delay for the next spawn.
    MaxSpawnDelay: int | None = None  # Maximum random delay for the next spawn.
    MaxNearbyEntities: int | None = None  # Maximum number of entities nearby.
    RequiredPlayerRange: int | None = None  # Radius in blocks that a player has to be within to spawn entities.
