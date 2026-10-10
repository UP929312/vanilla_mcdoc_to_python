"""
Generated from symbols.json for ::java::data::loot::condition::RandomChance
Local link to file: vanilla_mcdoc/data/loot/condition/RandomChance.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.number_provider.FloatNumberProviderRef import FloatNumberProviderRef


class RandomChance(GeneratedModel):
    chance: FloatNumberProviderRef  # Accepts a value between `0` & `1` (inclusive).
