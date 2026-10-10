"""
Generated from symbols.json for ::java::data::loot::function::LimitCount
Local link to file: vanilla_mcdoc/data/loot/function/LimitCount.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.data.loot.function.Conditions import Conditions

if TYPE_CHECKING:
    from vanilla_mcdoc.data.number_provider.IntNumberProviderRef import IntNumberProviderRef


class LimitStruct(GeneratedModel):
    min: IntNumberProviderRef | None = None
    max: IntNumberProviderRef | None = None


class LimitCount(Conditions):
    limit: LimitStruct  # Limits the count of the item to a range.
