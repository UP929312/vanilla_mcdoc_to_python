"""
Generated from symbols.json for ::java::data::loot::function::SetCustomData
Local link to file: vanilla_mcdoc/data/loot/function/SetCustomData.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.data.loot.function.Conditions import Conditions

if TYPE_CHECKING:
    from vanilla_mcdoc.world.component.CustomData import CustomData


class SetCustomData(Conditions):
    tag: CustomData
