"""
Generated from symbols.json for ::java::data::enchantment::effect_component::DamageProtectionEnchantmentEffect
Local link to file: vanilla_mcdoc/data/enchantment/effect_component/DamageProtectionEnchantmentEffect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.enchantment.effect.ValueEffect import ValueEffect
    from vanilla_mcdoc.data.predicate.Predicate import Predicate


class DamageProtectionEnchantmentEffect(GeneratedModel):
    requirements: Predicate | None = None  # Predicate context: Damage Parameters.
    effect: ValueEffect  # Damage reduction factor.  Provides `factor * 4%` of damage reduction, capped at 80%.
