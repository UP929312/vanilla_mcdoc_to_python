# Generated from symbols.json for ::java::world::block::structure_block::StructureBlock
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.block.BlockEntity import BlockEntity

if TYPE_CHECKING:
    from generated_symbols.world.block.structure_block.Mirror import Mirror
    from generated_symbols.world.block.structure_block.Mode import Mode
    from generated_symbols.world.block.structure_block.Rotation import Rotation


@dataclass(kw_only=True)
class StructureBlock(BlockEntity):
    name: str | None = None
    author: str | None = None  # Author of the structure.
    metadata: str | None = None  # Custom data for the structure. Stores the data id for "DATA" mode.
    posX: int | None = None  # Relative offset.
    posY: int | None = None  # Relative offset.
    posZ: int | None = None  # Relative offset.
    sizeX: int | None = None
    sizeY: int | None = None
    sizeZ: int | None = None
    rotation: Rotation | None = None
    mirror: Mirror | None = None
    mode: Mode | None = None
    ignoreEntities: bool | None = None
    showboundingbox: bool | None = None  # Whether to show the bounding box.
    powered: bool | None = None  # Whether it has been powered by redstone.
    showair: bool | None = None  # Whether to show invisible blocks inside the bounding box.
    strict: bool | None = None  # If set to `true`, the blocks in the placed structure will trigger block (entity) updates and shape updates. Defaults to `false`.
    integrity: float | None = None  # Chance for each block to stay.
    seed: int | None = None  # Seed for the integrity random.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::structure_block::StructureBlock": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::block::BlockEntity"
                }
            },
            {
                "kind": "pair",
                "key": "name",
                "type": {
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
                                            "value": "structure"
                                        }
                                    },
                                    "empty": {
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
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Author of the structure.",
                "key": "author",
                "type": {
                    "kind": "string"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Custom data for the structure. Stores the data id for \"DATA\" mode.",
                "key": "metadata",
                "type": {
                    "kind": "string"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Relative offset.",
                "key": "posX",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Relative offset.",
                "key": "posY",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Relative offset.",
                "key": "posZ",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "sizeX",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "sizeY",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "sizeZ",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "rotation",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::block::structure_block::Rotation"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "mirror",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::block::structure_block::Mirror"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "mode",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::block::structure_block::Mode"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "ignoreEntities",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether to show the bounding box.",
                "key": "showboundingbox",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether it has been powered by redstone.",
                "key": "powered",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether to show invisible blocks inside the bounding box.",
                "key": "showair",
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
                                "value": "1.21.5"
                            }
                        }
                    }
                ],
                "desc": "If set to `True`, the blocks in the placed structure will trigger block (entity) updates and shape updates. Defaults to `False`.",
                "key": "strict",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Chance for each block to stay.",
                "key": "integrity",
                "type": {
                    "kind": "float"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Seed for the integrity random.",
                "key": "seed",
                "type": {
                    "kind": "long",
                    "attributes": [
                        {
                            "name": "random"
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

