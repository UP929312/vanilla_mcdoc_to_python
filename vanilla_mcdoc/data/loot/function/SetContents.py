"""
Generated from symbols.json for ::java::data::loot::function::SetContents
Local link to file: vanilla_mcdoc/data/loot/function/SetContents.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.data.loot.function.Conditions import Conditions
from vanilla_mcdoc.minecraft_types import NamespacedId

if TYPE_CHECKING:
    from vanilla_mcdoc.data.loot.LootPoolEntry import LootPoolEntry
    from vanilla_mcdoc.data.loot.function.ContainerComponents import ContainerComponents


class SetContents(Conditions):
    component: NamespacedId[ContainerComponents]  # Describes target component to be filled with items.
    entries: list[LootPoolEntry]
