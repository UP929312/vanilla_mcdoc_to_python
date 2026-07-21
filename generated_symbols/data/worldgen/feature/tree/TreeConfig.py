# Generated from symbols.json for ::java::data::worldgen::feature::tree::TreeConfig
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.block_state_provider.BlockStateProvider import BlockStateProvider
    from generated_symbols.data.worldgen.feature.tree.FeatureSize import FeatureSize
    from generated_symbols.data.worldgen.feature.tree.FoliagePlacer import FoliagePlacer
    from generated_symbols.data.worldgen.feature.tree.RootPlacer import RootPlacer
    from generated_symbols.data.worldgen.feature.tree.TreeDecorator import TreeDecorator
    from generated_symbols.data.worldgen.feature.tree.TrunkPlacer import TrunkPlacer


@dataclass(kw_only=True)
class TreeConfig:
    minimum_size: FeatureSize
    below_trunk_provider: BlockStateProvider
    trunk_provider: BlockStateProvider
    foliage_provider: BlockStateProvider
    trunk_placer: TrunkPlacer
    foliage_placer: FoliagePlacer
    decorators: list[TreeDecorator]
    ignore_vines: bool | None = None
    root_placer: RootPlacer | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::tree::TreeConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.17"
                            }
                        }
                    }
                ],
                "key": "max_water_depth",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "ignore_vines",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.17"
                            }
                        }
                    }
                ],
                "key": "heightmap",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::HeightmapType"
                }
            },
            {
                "kind": "pair",
                "key": "minimum_size",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::tree::FeatureSize"
                }
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.17"
                            }
                        }
                    },
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.1"
                            }
                        }
                    }
                ],
                "key": "force_dirt",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.17"
                            }
                        }
                    },
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.1"
                            }
                        }
                    }
                ],
                "key": "dirt_provider",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::block_state_provider::BlockStateProvider"
                }
            },
            {
                "kind": "spread",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.1"
                            }
                        }
                    },
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.2"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "below_trunk_provider",
                            "type": {
                                "kind": "reference",
                                "path": "::java::data::worldgen::feature::block_state_provider::BlockStateProvider"
                            },
                            "optional": True
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.2"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "below_trunk_provider",
                            "type": {
                                "kind": "reference",
                                "path": "::java::data::worldgen::feature::block_state_provider::BlockStateProvider"
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.17"
                            }
                        }
                    },
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.18"
                            }
                        }
                    }
                ],
                "key": "sapling_provider",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::block_state_provider::BlockStateProvider"
                }
            },
            {
                "kind": "pair",
                "key": "trunk_provider",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::block_state_provider::BlockStateProvider"
                }
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.17"
                            }
                        }
                    }
                ],
                "key": "leaves_provider",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::block_state_provider::BlockStateProvider"
                }
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.17"
                            }
                        }
                    }
                ],
                "key": "foliage_provider",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::block_state_provider::BlockStateProvider"
                }
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.19"
                            }
                        }
                    }
                ],
                "key": "root_placer",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::tree::RootPlacer"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "trunk_placer",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::tree::TrunkPlacer"
                }
            },
            {
                "kind": "pair",
                "key": "foliage_placer",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::tree::FoliagePlacer"
                }
            },
            {
                "kind": "pair",
                "key": "decorators",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::feature::tree::TreeDecorator"
                    }
                }
            }
        ]
    }
}

