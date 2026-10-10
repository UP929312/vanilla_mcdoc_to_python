"""
Generated from symbols.json for ::java::data::loot::function::SetItem
Local link to file: vanilla_mcdoc/data/loot/function/SetItem.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.data.loot.function.Conditions import Conditions
from vanilla_mcdoc.minecraft_types import IdSpec


class SetItem(Conditions):
    item: Annotated[str, IdSpec(registry='item', exclude=('air',))]
