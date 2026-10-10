"""
Generated from symbols.json for ::java::world::block::container::ContainerBase
Local link to file: vanilla_mcdoc/world/block/container/ContainerBase.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.minecraft_types import IdSpec
from vanilla_mcdoc.world.block.BlockEntity import BlockEntity
from vanilla_mcdoc.world.block.Lockable import Lockable
from vanilla_mcdoc.world.block.Nameable import Nameable


class ContainerBase(BlockEntity, Lockable, Nameable):
    LootTable: Annotated[str, IdSpec(registry='loot_table', empty='allowed')] | None = None  # Loot table that will populate this container.
    LootTableSeed: int | None = None  # Seed of the loot table.
