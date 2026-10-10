"""
Generated from symbols.json for ::java::world::block::vault::Config
Local link to file: vanilla_mcdoc/world/block/vault/Config.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.world.item.ItemStack import ItemStack


class Config(GeneratedModel):
    key_item: ItemStack | None = None  # Item required to open the vault.
    loot_table: Annotated[str, IdSpec(registry='loot_table')] | None = None  # Defaults to "minecraft:chests/trial_chambers/reward".
    override_loot_table_to_display: Annotated[str, IdSpec(registry='loot_table')] | None = None  # The loot table to display items in the vault. Defaults to use the value in `loot_table` field.
    activation_range: float | None = None  # The range when the vault should activate.
    deactivation_range: float | None = None  # The range when the vault should deactivate.
