"""
Generated from symbols.json for ::java::world::block::vault::SharedData
Local link to file: vanilla_mcdoc/world/block/vault/SharedData.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import MinecraftUUID

if TYPE_CHECKING:
    from vanilla_mcdoc.world.item.ItemStack import ItemStack


class SharedData(GeneratedModel):
    display_item: ItemStack | None = None  # Item that is displayed to players when they are in range of the vault.
    connected_players: list[MinecraftUUID] | None = None
    connected_particles_range: float | None = None
