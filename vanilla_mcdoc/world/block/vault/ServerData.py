"""
Generated from symbols.json for ::java::world::block::vault::ServerData
Local link to file: vanilla_mcdoc/world/block/vault/ServerData.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.world.item.ItemStack import ItemStack


class ServerData(GeneratedModel):
    state_updating_resumes_at: int | None = None  # Ticks until the loot table is ran again to update the display item.
    rewarded_players: list[tuple[int, int, int, int]] | None = None  # When a player is in this list they can no longer open the vault, but other players can.
    items_to_eject: list[ItemStack] | None = None  # Items that are being ejected from the vault when it is opened. As each item is ejected, it is removed from this list, before ejection, it is previewed as the `display_item`.
    total_ejections_needed: int | None = None  # Number of items that the loot table started off the opening with, does not change while items are ejected.
