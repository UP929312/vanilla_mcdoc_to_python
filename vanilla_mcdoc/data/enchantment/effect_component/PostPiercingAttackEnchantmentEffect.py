"""
Generated from symbols.json for ::java::data::enchantment::effect_component::PostPiercingAttackEnchantmentEffect
Local link to file: vanilla_mcdoc/data/enchantment/effect_component/PostPiercingAttackEnchantmentEffect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.enchantment.effect.EntityEffect import EntityEffect
    from vanilla_mcdoc.data.predicate.Predicate import Predicate


class PostPiercingAttackEnchantmentEffect(GeneratedModel):
    requirements: Predicate | None = None  # Predicate context: Damage Parameters.
    effect: EntityEffect  # The effect to apply on attacker.
