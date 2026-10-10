"""
Generated from symbols.json for ::java::world::block::brushable_block::BrushableBlock
Local link to file: vanilla_mcdoc/world/block/brushable_block/BrushableBlock.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.minecraft_types import IdSpec
from vanilla_mcdoc.world.block.BlockEntity import BlockEntity

if TYPE_CHECKING:
    from vanilla_mcdoc.util.direction.DirectionByte import DirectionByte
    from vanilla_mcdoc.world.item.ItemStack import ItemStack


class BrushableBlock(BlockEntity):
    LootTable: Annotated[str, IdSpec(registry='loot_table', empty='allowed')] | None = None  # Loot table that will decide the brushed loot.
    LootTableSeed: int | None = None  # Seed of the loot table.
    item: ItemStack | None = None  # Item that was rolled from the loot table, which is currently peeking out.
    hit_direction: DirectionByte | None = None  # Direction of the block that was interacted with. Write-only, is not saved by the game.
