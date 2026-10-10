"""
Generated from symbols.json for ::java::data::worldgen::structure::SpawnOverride
Local link to file: vanilla_mcdoc/data/worldgen/structure/SpawnOverride.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.biome.SpawnerData import SpawnerData
    from vanilla_mcdoc.data.worldgen.structure.BoundingBox import BoundingBox
    from vanilla_mcdoc.util.FlatWeightedList import FlatWeightedList


class SpawnOverride(GeneratedModel):
    bounding_box: BoundingBox
    spawns: FlatWeightedList[SpawnerData]
