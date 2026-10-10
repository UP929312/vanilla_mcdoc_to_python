"""
Generated from symbols.json for ::java::world::entity::falling_block::FallingBlock
Local link to file: vanilla_mcdoc/world/entity/falling_block/FallingBlock.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.world.entity.EntityBase import EntityBase

if TYPE_CHECKING:
    from vanilla_mcdoc.util.BlockState import BlockState


class TileEntityDataStruct(GeneratedModel):
    pass


class FallingBlock(EntityBase):
    TileEntityData: TileEntityDataStruct | None = None  # NBT data for the placed block.
    BlockState_: BlockState | None = Field(default=None, alias='BlockState')  # Block state for the placed block. Defaults to sand.
    Time: int | None = None  # Ticks it has existed.
    DropItem: bool | None = None  # Whether it should drop as a block when destroyed.
    HurtEntities: bool | None = None  # Whether this it should hurt entities.
    FallHurtMax: int | None = None  # Maximum damage it should deal.
    FallHurtAmount: float | None = None  # Damage multiplier.
    CancelDrop: bool | None = None  # Whether the block should be destroyed instead of placed after landing on a solid block. When `true`, the block is not dropped as an item, even if the DropItem tag is set to `true`. However, if the entity is deleted due to its Time value being too high, this tag is ignored and an item is dropped depending on the `DropItem` tag. Defaults to `1` for falling suspicious sand and suspicious gravel, and `0` for the other vanilla falling blocks and any summoned falling block.
