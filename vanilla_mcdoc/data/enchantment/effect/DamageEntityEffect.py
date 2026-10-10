"""
Generated from symbols.json for ::java::data::enchantment::effect::DamageEntityEffect
Local link to file: vanilla_mcdoc/data/enchantment/effect/DamageEntityEffect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.enchantment.LevelBasedValue import LevelBasedValue


class DamageEntityEffect(GeneratedModel):
    damage_type: Annotated[str, IdSpec(registry='damage_type')]
    min_damage: LevelBasedValue  # Amount of damage is randomized within the given min/max span.
    max_damage: LevelBasedValue
