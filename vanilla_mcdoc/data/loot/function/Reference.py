"""
Generated from symbols.json for ::java::data::loot::function::Reference
Local link to file: vanilla_mcdoc/data/loot/function/Reference.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.data.loot.function.Conditions import Conditions
from vanilla_mcdoc.minecraft_types import IdSpec


class Reference(Conditions):
    name: Annotated[str, IdSpec(registry='item_modifier')]  # Item modifier to reference.
