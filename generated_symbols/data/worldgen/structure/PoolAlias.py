"""
Generated from symbols.json for ::java::data::worldgen::structure::PoolAlias
Local link to file: generated_symbols/data/worldgen/structure/PoolAlias.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Field

from generated_symbols.data.worldgen.structure.DirectPoolAlias import DirectPoolAlias
from generated_symbols.data.worldgen.structure.RandomGroupPoolAlias import RandomGroupPoolAlias
from generated_symbols.data.worldgen.structure.RandomPoolAlias import RandomPoolAlias


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


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::structure::PoolAlias": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "worldgen/pool_alias_binding"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "type"
                            ]
                        }
                    ],
                    "registry": "minecraft:worldgen/pool_alias_binding"
                }
            }
        ]
    }
}

