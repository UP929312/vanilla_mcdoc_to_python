"""
Generated from symbols.json for ::java::data::enchantment::effect_component::DamageImmunityEnchantmentEffect
Local link to file: vanilla_mcdoc/data/enchantment/effect_component/DamageImmunityEnchantmentEffect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.predicate.Predicate import Predicate


class EffectStruct(GeneratedModel):
    pass


class DamageImmunityEnchantmentEffect(GeneratedModel):
    requirements: Predicate | None = None  # Predicate context: Damage Parameters.
    effect: EffectStruct  # Dummy value; this is a boolean effect.
