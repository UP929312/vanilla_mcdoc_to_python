"""
Generated from symbols.json for ::java::data::loot::IntRange
Local link to file: vanilla_mcdoc/data/loot/IntRange.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.number_provider.IntNumberProviderRef import IntNumberProviderRef


class IntRangeStruct(GeneratedModel):
    min: IntNumberProviderRef | None = None
    max: IntNumberProviderRef | None = None


type IntRange = IntNumberProviderRef | IntRangeStruct
