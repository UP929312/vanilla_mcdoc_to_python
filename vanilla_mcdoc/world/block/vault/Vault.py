"""
Generated from symbols.json for ::java::world::block::vault::Vault
Local link to file: vanilla_mcdoc/world/block/vault/Vault.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec, MinecraftUUID

if TYPE_CHECKING:
    from vanilla_mcdoc.world.item.ItemStack import ItemStack


class ServerDataStruct(GeneratedModel):
    state_updating_resumes_at: int | None = None  # Ticks until the loot table is ran again to update the display item.
    rewarded_players: list[tuple[int, int, int, int]] | None = None  # When a player is in this list they can no longer open the vault, but other players can.
    items_to_eject: list[ItemStack] | None = None  # Items that are being ejected from the vault when it is opened. As each item is ejected, it is removed from this list, before ejection, it is previewed as the `display_item`.
    total_ejections_needed: int | None = None  # Number of items that the loot table started off the opening with, does not change while items are ejected.


class ConfigStruct(GeneratedModel):
    key_item: ItemStack | None = None  # Item required to open the vault.
    loot_table: Annotated[str, IdSpec(registry='loot_table')] | None = None  # Defaults to "minecraft:chests/trial_chambers/reward".
    override_loot_table_to_display: Annotated[str, IdSpec(registry='loot_table')] | None = None  # The loot table to display items in the vault. Defaults to use the value in `loot_table` field.
    activation_range: float | None = None  # The range when the vault should activate.
    deactivation_range: float | None = None  # The range when the vault should deactivate.


class SharedDataStruct(GeneratedModel):
    display_item: ItemStack | None = None  # Item that is displayed to players when they are in range of the vault.
    connected_players: list[MinecraftUUID] | None = None
    connected_particles_range: float | None = None


class Vault(GeneratedModel):
    server_data: ServerDataStruct | None = None
    config: ConfigStruct | None = None
    shared_data: SharedDataStruct | None = None  # When a player is in range of the vault, the same display item will be shown to all players. This is also used for the items that are being ejected from the vault.
