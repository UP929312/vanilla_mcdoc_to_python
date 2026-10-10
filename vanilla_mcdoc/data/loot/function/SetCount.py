"""
Generated from symbols.json for ::java::data::loot::function::SetCount
Local link to file: vanilla_mcdoc/data/loot/function/SetCount.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.data.loot.function.Conditions import Conditions

if TYPE_CHECKING:
    from vanilla_mcdoc.data.number_provider.IntNumberProviderRef import IntNumberProviderRef


class SetCount(Conditions):
    count: IntNumberProviderRef
    add: bool | None = None  # Whether to add to the existing count. Defaults to `false`.
