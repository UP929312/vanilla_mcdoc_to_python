"""
Generated from symbols.json for ::java::world::block::structure_block::StructureBlock
Local link to file: vanilla_mcdoc/world/block/structure_block/StructureBlock.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.minecraft_types import IdSpec
from vanilla_mcdoc.world.block.BlockEntity import BlockEntity

if TYPE_CHECKING:
    from vanilla_mcdoc.world.block.structure_block.Mirror import Mirror
    from vanilla_mcdoc.world.block.structure_block.Mode import Mode
    from vanilla_mcdoc.world.block.structure_block.Rotation import Rotation


class StructureBlock(BlockEntity):
    name: Annotated[str, IdSpec(registry='structure', empty='allowed')] | None = None
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
