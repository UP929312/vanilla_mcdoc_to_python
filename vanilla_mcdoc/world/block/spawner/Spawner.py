"""
Generated from symbols.json for ::java::world::block::spawner::Spawner
Local link to file: vanilla_mcdoc/world/block/spawner/Spawner.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.world.block.BlockEntity import BlockEntity

if TYPE_CHECKING:
    from vanilla_mcdoc.world.block.spawner.SpawnPotential import SpawnPotential
    from vanilla_mcdoc.world.block.spawner.SpawnerEntry import SpawnerEntry


class Spawner(BlockEntity):
    SpawnPotentials: list[SpawnPotential] | None = None  # Entities that can be placed.
    SpawnData: SpawnerEntry | None = None  # Data for the next mob to spawn. Overwritten by `SpawnPotentials`.
    SpawnCount: int | None = None  # Number of entities that will be placed.
    SpawnRange: int | None = None  # Range that the spawned entities will be placed.
    Delay: int | None = None  # Ticks until the next spawn.
    MinSpawnDelay: int | None = None  # Minimum random delay for the next spawn.
    MaxSpawnDelay: int | None = None  # Maximum random delay for the next spawn.
    MaxNearbyEntities: int | None = None  # Maximum number of entities nearby.
    RequiredPlayerRange: int | None = None  # Radius in blocks that a player has to be within to spawn entities.
