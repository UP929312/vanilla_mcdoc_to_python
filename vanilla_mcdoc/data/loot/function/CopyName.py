"""
Generated from symbols.json for ::java::data::loot::function::CopyName
Local link to file: vanilla_mcdoc/data/loot/function/CopyName.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.data.loot.function.Conditions import Conditions

if TYPE_CHECKING:
    from vanilla_mcdoc.data.loot.BlockEntityTarget import BlockEntityTarget
    from vanilla_mcdoc.data.loot.EntityTarget import EntityTarget


class CopyName(Conditions):
    source: EntityTarget | BlockEntityTarget
