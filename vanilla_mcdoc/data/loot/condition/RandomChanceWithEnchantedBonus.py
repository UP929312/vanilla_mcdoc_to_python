"""
Generated from symbols.json for ::java::data::loot::condition::RandomChanceWithEnchantedBonus
Local link to file: vanilla_mcdoc/data/loot/condition/RandomChanceWithEnchantedBonus.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.enchantment.LevelBasedValue import LevelBasedValue


class RandomChanceWithEnchantedBonus(GeneratedModel):
    unenchanted_chance: Annotated[float, Field(ge=0, le=1)]
    enchanted_chance: LevelBasedValue
    enchantment: Annotated[str, IdSpec(registry='enchantment')]
