"""
Generated from symbols.json for ::java::data::worldgen::feature::RandomNeighborSpreadConfig
Local link to file: generated_symbols/data/worldgen/feature/RandomNeighborSpreadConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from generated_symbols.base import GeneratedModel
from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.IntProvider import IntProvider
    from generated_symbols.data.worldgen.feature.block_predicate.BlockPredicate import BlockPredicate
    from generated_symbols.data.worldgen.feature.block_state_provider.BlockStateProviderRef import BlockStateProviderRef
    from generated_symbols.registry.KnownBlockId import KnownBlockId


class RandomNeighborSpreadConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    block: BlockStateProviderRef
    accepted_neighbors: Annotated[str, IdSpec(registry='block', tags='allowed')] | KnownBlockId | list[Annotated[str, IdSpec(registry='block')] | KnownBlockId]
    can_replace: BlockPredicate
    attempts: IntProvider[Annotated[int, Field(ge=1, le=3000)]] | Annotated[int, Field(ge=1, le=3000)]
    xz_offset: IntProvider[Annotated[int, Field(ge=-16, le=16)]] | Annotated[int, Field(ge=-16, le=16)]
    y_offset: IntProvider[Annotated[int, Field(ge=-16, le=16)]] | Annotated[int, Field(ge=-16, le=16)]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::RandomNeighborSpreadConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "block",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::block_state_provider::BlockStateProviderRef"
                }
            },
            {
                "kind": "pair",
                "key": "accepted_neighbors",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "tree",
                                        "values": {
                                            "registry": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "block"
                                                }
                                            },
                                            "tags": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "allowed"
                                                }
                                            }
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "list",
                            "item": {
                                "kind": "string",
                                "attributes": [
                                    {
                                        "name": "id",
                                        "value": {
                                            "kind": "literal",
                                            "value": {
                                                "kind": "string",
                                                "value": "block"
                                            }
                                        }
                                    }
                                ]
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "can_replace",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::block_predicate::BlockPredicate"
                }
            },
            {
                "kind": "pair",
                "key": "attempts",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::IntProvider"
                    },
                    "typeArgs": [
                        {
                            "kind": "int",
                            "valueRange": {
                                "kind": 0,
                                "min": 1,
                                "max": 3000
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "xz_offset",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::IntProvider"
                    },
                    "typeArgs": [
                        {
                            "kind": "int",
                            "valueRange": {
                                "kind": 0,
                                "min": -16,
                                "max": 16
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "y_offset",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::IntProvider"
                    },
                    "typeArgs": [
                        {
                            "kind": "int",
                            "valueRange": {
                                "kind": 0,
                                "min": -16,
                                "max": 16
                            }
                        }
                    ]
                }
            }
        ]
    }
}

