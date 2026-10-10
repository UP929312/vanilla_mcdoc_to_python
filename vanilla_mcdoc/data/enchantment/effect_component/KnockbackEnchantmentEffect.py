"""
Generated from symbols.json for ::java::data::enchantment::effect_component::KnockbackEnchantmentEffect
Local link to file: vanilla_mcdoc/data/enchantment/effect_component/KnockbackEnchantmentEffect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.enchantment.effect.ValueEffect import ValueEffect
    from vanilla_mcdoc.data.predicate.Predicate import Predicate


class KnockbackEnchantmentEffect(GeneratedModel):
    requirements: Predicate | None = None  # Predicate context: Damage Parameters.
    effect: ValueEffect  # Amount of knockback being applied.
