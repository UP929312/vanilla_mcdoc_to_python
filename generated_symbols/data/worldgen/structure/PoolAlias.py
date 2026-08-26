"""
Generated from symbols.json for ::java::data::worldgen::structure::PoolAlias
Local link to file: generated_symbols/data/worldgen/structure/PoolAlias.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Literal

from generated_symbols.data.worldgen.structure.DirectPoolAlias import DirectPoolAlias
from generated_symbols.data.worldgen.structure.RandomGroupPoolAlias import RandomGroupPoolAlias
from generated_symbols.data.worldgen.structure.RandomPoolAlias import RandomPoolAlias


@dataclass(kw_only=True)
class PoolAliasDirect(DirectPoolAlias):
    type: Literal['minecraft:direct']


@dataclass(kw_only=True)
class PoolAliasRandom(RandomPoolAlias):
    type: Literal['minecraft:random']


@dataclass(kw_only=True)
class PoolAliasRandomGroup(RandomGroupPoolAlias):
    type: Literal['minecraft:random_group']


type PoolAlias = PoolAliasDirect | PoolAliasRandom | PoolAliasRandomGroup


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

