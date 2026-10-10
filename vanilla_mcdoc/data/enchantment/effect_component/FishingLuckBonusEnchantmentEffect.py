"""
Generated from symbols.json for ::java::data::enchantment::effect_component::FishingLuckBonusEnchantmentEffect
Local link to file: vanilla_mcdoc/data/enchantment/effect_component/FishingLuckBonusEnchantmentEffect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.enchantment.effect.ValueEffect import ValueEffect
    from vanilla_mcdoc.data.predicate.Predicate import Predicate


class FishingLuckBonusEnchantmentEffect(GeneratedModel):
    requirements: Predicate | None = None  # Predicate context: Entity Parameters.  `this` is the player fishing.
    effect: ValueEffect  # Amount of luck being added.
