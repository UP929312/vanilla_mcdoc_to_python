"""
Generated from symbols.json for ::java::data::loot::function::SetPotion
Local link to file: vanilla_mcdoc/data/loot/function/SetPotion.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.data.loot.function.Conditions import Conditions
from vanilla_mcdoc.minecraft_types import IdSpec


class SetPotion(Conditions):
    id: Annotated[str, IdSpec(registry='potion')]  # The potion identifier.
