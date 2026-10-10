"""
Generated from symbols.json for ::java::data::enchantment::level_based_value::LookupLevelValue
Local link to file: vanilla_mcdoc/data/enchantment/level_based_value/LookupLevelValue.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.enchantment.level_based_value.LevelBasedValue import LevelBasedValue


class LookupLevelValue(GeneratedModel):
    values: Annotated[list[LevelBasedValue], Field(min_length=1)]  # Indexed by `level - 1` to apply, if present
    fallback: LevelBasedValue  # Applied if the level is greater than the size of `values`.
