"""
Generated from symbols.json for ::java::data::worldgen::structure::PoolAlias
Local link to file: vanilla_mcdoc/data/worldgen/structure/PoolAlias.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Discriminator, Tag

from vanilla_mcdoc.base import tag_of
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
    Annotated[PoolAliasDirect, Tag('minecraft:direct')]
    | Annotated[PoolAliasRandom, Tag('minecraft:random')]
    | Annotated[PoolAliasRandomGroup, Tag('minecraft:random_group')],
    Discriminator(tag_of('type')),
]
