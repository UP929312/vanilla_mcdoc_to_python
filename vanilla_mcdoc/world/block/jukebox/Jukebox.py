"""
Generated from symbols.json for ::java::world::block::jukebox::Jukebox
Local link to file: vanilla_mcdoc/world/block/jukebox/Jukebox.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.world.block.BlockEntity import BlockEntity

if TYPE_CHECKING:
    from vanilla_mcdoc.world.item.ItemStack import ItemStack


class Jukebox(BlockEntity):
    RecordItem: ItemStack | None = None
    ticks_since_song_started: int | None = None
