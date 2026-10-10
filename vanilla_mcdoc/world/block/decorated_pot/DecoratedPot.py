"""
Generated from symbols.json for ::java::world::block::decorated_pot::DecoratedPot
Local link to file: vanilla_mcdoc/world/block/decorated_pot/DecoratedPot.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.minecraft_types import IdSpec
from vanilla_mcdoc.world.block.BlockEntity import BlockEntity

if TYPE_CHECKING:
    from vanilla_mcdoc.world.component.block.PotDecorations import PotDecorations
    from vanilla_mcdoc.world.item.ItemStack import ItemStack


class DecoratedPot(BlockEntity):
    sherds: PotDecorations | None = None  # Item ID of what was used for each side of the pot.  Decoration textures are determined by `provides_pottery_pattern` component on the sherd items.
    LootTable: Annotated[str, IdSpec(registry='loot_table', empty='allowed')] | None = None  # Loot table that will populate this container.
    LootTableSeed: int | None = None  # Seed of the loot table.
    item: ItemStack | None = None
