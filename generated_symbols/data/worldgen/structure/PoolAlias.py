# Generated from symbols.json for ::java::data::worldgen::structure::PoolAlias
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

from runtime_metadata import IdSpec

if TYPE_CHECKING:
    from generated_symbols.util.NonEmptyWeightedList import NonEmptyWeightedList


@dataclass(kw_only=True)
class PoolAliasDirect:
    type: Literal['minecraft:direct']
    alias: Annotated[str, IdSpec()]
    target: Annotated[str, IdSpec(registry='worldgen/template_pool')]


@dataclass(kw_only=True)
class PoolAliasRandom:
    type: Literal['minecraft:random']
    alias: Annotated[str, IdSpec()]
    targets: NonEmptyWeightedList[Annotated[str, IdSpec(registry='worldgen/template_pool')]]


@dataclass(kw_only=True)
class PoolAliasRandomGroup:
    type: Literal['minecraft:random_group']
    groups: NonEmptyWeightedList[list[PoolAlias]]


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

