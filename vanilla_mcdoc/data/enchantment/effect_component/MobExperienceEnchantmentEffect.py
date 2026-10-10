"""
Generated from symbols.json for ::java::data::enchantment::effect_component::MobExperienceEnchantmentEffect
Local link to file: vanilla_mcdoc/data/enchantment/effect_component/MobExperienceEnchantmentEffect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.enchantment.effect.ValueEffect import ValueEffect
    from vanilla_mcdoc.data.predicate.Predicate import Predicate


class MobExperienceEnchantmentEffect(GeneratedModel):
    requirements: Predicate | None = None  # Predicate context: Entity Parameters.  `this` is the killed mob.
    effect: ValueEffect  # Amount of experience awarded.
