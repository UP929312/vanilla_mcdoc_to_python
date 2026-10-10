"""
Generated from symbols.json for ::java::data::loot::function::SetComponents
Local link to file: vanilla_mcdoc/data/loot/function/SetComponents.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.data.loot.function.Conditions import Conditions

if TYPE_CHECKING:
    from vanilla_mcdoc.world.component.DataComponentPatch import DataComponentPatch


class SetComponents(Conditions):
    components: DataComponentPatch
