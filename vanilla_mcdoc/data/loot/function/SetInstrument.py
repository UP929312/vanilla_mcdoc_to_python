"""
Generated from symbols.json for ::java::data::loot::function::SetInstrument
Local link to file: vanilla_mcdoc/data/loot/function/SetInstrument.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.data.loot.function.Conditions import Conditions
from vanilla_mcdoc.minecraft_types import IdSpec


class SetInstrument(Conditions):
    options: Annotated[str, IdSpec(registry='instrument', tags='allowed')] | list[Annotated[str, IdSpec(registry='instrument')]]  # Sets the instrument tag for a goat horn.
