"""
Generated from symbols.json for ::java::data::worldgen::biome::NaturalMobSpawns
Local link to file: vanilla_mcdoc/data/worldgen/biome/NaturalMobSpawns.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.biome.MobSpawnCost import MobSpawnCost
    from vanilla_mcdoc.data.worldgen.biome.SpawnerDataMap import SpawnerDataMap
    from vanilla_mcdoc.registry.KnownEntityId import KnownEntityId


class NaturalMobSpawns(GeneratedModel):
    spawns_by_category: SpawnerDataMap
    spawn_costs: dict[Annotated[str, IdSpec(registry='entity')] | KnownEntityId, MobSpawnCost]
