"""
Generated from symbols.json for ::java::data::worldgen::structure::RandomGroupPoolAlias
Local link to file: vanilla_mcdoc/data/worldgen/structure/RandomGroupPoolAlias.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.structure.PoolAlias import PoolAlias
    from vanilla_mcdoc.util.NonEmptyWeightedList import NonEmptyWeightedList


class RandomGroupPoolAlias(GeneratedModel):
    groups: NonEmptyWeightedList[list[PoolAlias]]
