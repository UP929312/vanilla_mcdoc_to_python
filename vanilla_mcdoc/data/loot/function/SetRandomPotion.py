"""
Generated from symbols.json for ::java::data::loot::function::SetRandomPotion
Local link to file: vanilla_mcdoc/data/loot/function/SetRandomPotion.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.data.loot.function.Conditions import Conditions
from vanilla_mcdoc.minecraft_types import IdSpec


class SetRandomPotion(Conditions):
    options: Annotated[str, IdSpec(registry='potion', tags='allowed')] | list[Annotated[str, IdSpec(registry='potion')]] | None = None  # Possible potions to select from. Defaults to all potions.
