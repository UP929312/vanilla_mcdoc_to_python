# Generated from symbols.json for ::java::data::structure::StructureNBT
from dataclasses import dataclass
from typing import Annotated, Any
from generated_symbols.data.structure.BlockPalette import BlockPalette


@dataclass(kw_only=True)
class StructureNBT(BlockPalette):
    DataVersion: Annotated[int, 'Range | Min `0` and above | inclusive']  # [Data version](https://minecraft.wiki/w/Data_version).
    size: tuple[Annotated[int, 'Range | Min `0` and above | inclusive'], Annotated[int, 'Range | Min `0` and above | inclusive'], Annotated[int, 'Range | Min `0` and above | inclusive']]
    blocks: list[Any]
    entities: list[Any]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::structure::StructureNBT": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "[Data version](https://minecraft.wiki/w/Data_version).",
                "key": "DataVersion",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                }
            },
            {
                "kind": "pair",
                "key": "size",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "int",
                        "valueRange": {
                            "kind": 0,
                            "min": 0
                        }
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 3,
                        "max": 3
                    }
                }
            },
            {
                "kind": "pair",
                "key": "blocks",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "struct",
                        "fields": [
                            {
                                "kind": "pair",
                                "key": "state",
                                "type": {
                                    "kind": "int",
                                    "valueRange": {
                                        "kind": 0,
                                        "min": 0
                                    }
                                }
                            },
                            {
                                "kind": "pair",
                                "key": "pos",
                                "type": {
                                    "kind": "list",
                                    "item": {
                                        "kind": "int",
                                        "valueRange": {
                                            "kind": 0,
                                            "min": 0
                                        }
                                    },
                                    "lengthRange": {
                                        "kind": 0,
                                        "min": 3,
                                        "max": 3
                                    }
                                }
                            },
                            {
                                "kind": "pair",
                                "key": "nbt",
                                "type": {
                                    "kind": "dispatcher",
                                    "parallelIndices": [
                                        {
                                            "kind": "static",
                                            "value": "%fallback"
                                        }
                                    ],
                                    "registry": "minecraft:block"
                                },
                                "optional": True
                            }
                        ]
                    }
                }
            },
            {
                "kind": "pair",
                "key": "entities",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "struct",
                        "fields": [
                            {
                                "kind": "pair",
                                "key": "pos",
                                "type": {
                                    "kind": "list",
                                    "item": {
                                        "kind": "double",
                                        "valueRange": {
                                            "kind": 0,
                                            "min": 0
                                        }
                                    },
                                    "lengthRange": {
                                        "kind": 0,
                                        "min": 3,
                                        "max": 3
                                    }
                                }
                            },
                            {
                                "kind": "pair",
                                "key": "blockPos",
                                "type": {
                                    "kind": "list",
                                    "item": {
                                        "kind": "int",
                                        "valueRange": {
                                            "kind": 0,
                                            "min": 0
                                        }
                                    },
                                    "lengthRange": {
                                        "kind": 0,
                                        "min": 3,
                                        "max": 3
                                    }
                                }
                            },
                            {
                                "kind": "pair",
                                "key": "nbt",
                                "type": {
                                    "kind": "reference",
                                    "path": "::java::world::entity::AnyEntity"
                                }
                            }
                        ]
                    }
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::structure::BlockPalette"
                }
            }
        ]
    }
}

