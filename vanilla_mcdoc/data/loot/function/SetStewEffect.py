"""
Generated from symbols.json for ::java::data::loot::function::SetStewEffect
Local link to file: vanilla_mcdoc/data/loot/function/SetStewEffect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.data.loot.function.Conditions import Conditions

if TYPE_CHECKING:
    from vanilla_mcdoc.data.loot.function.StewEffect import StewEffect


class SetStewEffect(Conditions):
    effects: list[StewEffect] | None = None  # Sets the status effects for suspicious stew.
