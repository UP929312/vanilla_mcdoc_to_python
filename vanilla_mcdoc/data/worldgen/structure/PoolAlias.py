"""
Generated from symbols.json for ::java::data::worldgen::structure::PoolAlias
Local link to file: vanilla_mcdoc/data/worldgen/structure/PoolAlias.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Field

from vanilla_mcdoc.data.worldgen.structure.DirectPoolAlias import DirectPoolAlias
from vanilla_mcdoc.data.worldgen.structure.RandomGroupPoolAlias import RandomGroupPoolAlias
from vanilla_mcdoc.data.worldgen.structure.RandomPoolAlias import RandomPoolAlias


class PoolAliasDirect(DirectPoolAlias):
    type: Literal['minecraft:direct', 'direct'] = 'minecraft:direct'


class PoolAliasRandom(RandomPoolAlias):
    type: Literal['minecraft:random', 'random'] = 'minecraft:random'


class PoolAliasRandomGroup(RandomGroupPoolAlias):
    type: Literal['minecraft:random_group', 'random_group'] = 'minecraft:random_group'


type PoolAlias = Annotated[
    PoolAliasDirect | PoolAliasRandom | PoolAliasRandomGroup,
    Field(discriminator='type'),
]
