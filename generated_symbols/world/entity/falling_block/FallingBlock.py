# Generated from symbols.json for ::java::world::entity::falling_block::FallingBlock
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any
from generated_symbols.world.entity.EntityBase import EntityBase

if TYPE_CHECKING:
    from generated_symbols.util.BlockState import BlockState


@dataclass(kw_only=True)
class FallingBlock(EntityBase):
    TileEntityData: Any | None = None  # NBT data for the placed block.
    BlockState: BlockState | None = None  # Block state for the placed block. Defaults to sand.
    Time: int | None = None  # Ticks it has existed.
    DropItem: bool | None = None  # Whether it should drop as a block when destroyed.
    HurtEntities: bool | None = None  # Whether this it should hurt entities.
    FallHurtMax: int | None = None  # Maximum damage it should deal.
    FallHurtAmount: float | None = None  # Damage multiplier.
    CancelDrop: bool | None = None  # Whether the block should be destroyed instead of placed after landing on a solid block. When `true`, the block is not dropped as an item, even if the DropItem tag is set to `true`. However, if the entity is deleted due to its Time value being too high, this tag is ignored and an item is dropped depending on the `DropItem` tag. Defaults to `1` for falling suspicious sand and suspicious gravel, and `0` for the other vanilla falling blocks and any summoned falling block.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::falling_block::FallingBlock": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::EntityBase"
                }
            },
            {
                "kind": "pair",
                "desc": "NBT data for the placed block.",
                "key": "TileEntityData",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "BlockState",
                                "Name"
                            ]
                        }
                    ],
                    "registry": "minecraft:block"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Block state for the placed block. Defaults to sand.",
                "key": "BlockState",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::BlockState"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Ticks it has existed.",
                "key": "Time",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether it should drop as a block when destroyed.",
                "key": "DropItem",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether this it should hurt entities.",
                "key": "HurtEntities",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Maximum damage it should deal.",
                "key": "FallHurtMax",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Damage multiplier.",
                "key": "FallHurtAmount",
                "type": {
                    "kind": "float"
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
                                "value": "1.20"
                            }
                        }
                    }
                ],
                "desc": "Whether the block should be destroyed instead of placed after landing on a solid block.\nWhen `True`, the block is not dropped as an item, even if the DropItem tag is set to `True`.\nHowever, if the entity is deleted due to its Time value being too high, this tag is ignored and an item is dropped depending on the `DropItem` tag.\nDefaults to `1` for falling suspicious sand and suspicious gravel, and `0` for the other vanilla falling blocks and any summoned falling block.",
                "key": "CancelDrop",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

