"""
Generated from symbols.json for ::java::world::item::BlockItem
Local link to file: vanilla_mcdoc/world/item/BlockItem.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.world.item.ItemBase import ItemBase

if TYPE_CHECKING:
    from vanilla_mcdoc.world.block.BlockEntityData import BlockEntityData


class BlockItem(ItemBase):
    BlockEntityTag: BlockEntityData | None = None
    BlockStateTag: dict[str, str] | None = None  # Blockstate that the placed block will have.
