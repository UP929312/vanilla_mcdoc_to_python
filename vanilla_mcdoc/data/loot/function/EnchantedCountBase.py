"""
Generated from symbols.json for ::java::data::loot::function::EnchantedCountBase
Local link to file: vanilla_mcdoc/data/loot/function/EnchantedCountBase.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.number_provider.FloatNumberProviderRef import FloatNumberProviderRef


class EnchantedCountBase(GeneratedModel):
    count: FloatNumberProviderRef  # Rounded *after* the number was multiplied by the looting level.
    limit: int | None = None  # Limits the count of the item to a range.
