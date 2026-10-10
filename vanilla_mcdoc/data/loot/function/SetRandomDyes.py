"""
Generated from symbols.json for ::java::data::loot::function::SetRandomDyes
Local link to file: vanilla_mcdoc/data/loot/function/SetRandomDyes.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.data.loot.function.Conditions import Conditions

if TYPE_CHECKING:
    from vanilla_mcdoc.data.number_provider.IntNumberProviderRef import IntNumberProviderRef


class SetRandomDyes(Conditions):
    number_of_dyes: IntNumberProviderRef  # Applies specified number of random dyes to the item.  For example, one possible outcome of `"number_of_dyes": 2` is `#2C3065`, which is the combination of a blue dye and a black dye.  The same dye color can be selected multiple times.
