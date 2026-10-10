"""
Generated from symbols.json for ::java::data::item_modifier::ItemModifier
Local link to file: vanilla_mcdoc/data/item_modifier/ItemModifier.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.loot.LootFunction import LootFunction


type ItemModifier = LootFunction | list[ItemModifier] | Annotated[str, IdSpec(registry='item_modifier', tags='allowed')]
