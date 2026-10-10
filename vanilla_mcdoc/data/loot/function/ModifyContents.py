"""
Generated from symbols.json for ::java::data::loot::function::ModifyContents
Local link to file: vanilla_mcdoc/data/loot/function/ModifyContents.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.data.loot.function.Conditions import Conditions

if TYPE_CHECKING:
    from vanilla_mcdoc.data.item_modifier.ItemModifier import ItemModifier
    from vanilla_mcdoc.data.loot.function.ContainerComponents import ContainerComponents


class ModifyContents(Conditions):
    component: ContainerComponents  # Describes target component's items to modify.
    modifier: ItemModifier  # Applied to every item inside container.
