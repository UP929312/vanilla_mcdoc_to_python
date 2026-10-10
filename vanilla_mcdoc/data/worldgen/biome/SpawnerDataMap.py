"""
Generated from symbols.json for ::java::data::worldgen::biome::SpawnerDataMap
Local link to file: vanilla_mcdoc/data/worldgen/biome/SpawnerDataMap.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.biome.MobCategory import MobCategory
    from vanilla_mcdoc.data.worldgen.biome.SpawnerData import SpawnerData
    from vanilla_mcdoc.util.FlatWeightedList import FlatWeightedList


type SpawnerDataMap = dict[MobCategory, FlatWeightedList[SpawnerData]]
