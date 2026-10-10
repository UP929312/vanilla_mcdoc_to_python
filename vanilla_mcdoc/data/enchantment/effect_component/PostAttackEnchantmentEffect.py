"""
Generated from symbols.json for ::java::data::enchantment::effect_component::PostAttackEnchantmentEffect
Local link to file: vanilla_mcdoc/data/enchantment/effect_component/PostAttackEnchantmentEffect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.enchantment.effect.EntityEffect import EntityEffect
    from vanilla_mcdoc.data.enchantment.effect_component.AttackTarget import AttackTarget
    from vanilla_mcdoc.data.predicate.Predicate import Predicate


class PostAttackEnchantmentEffect(GeneratedModel):
    requirements: Predicate | None = None  # Predicate context: Damage Parameters.
    effect: EntityEffect  # Examples: - A Fire Aspect Enchant would specify that when the attacker is enchanted, the `ignite` effect is applied, and the affected party is the victim. - Thorns would specify that when the victim is enchanted, the `damage_entity` effect is applied, and the affected party is the attacker.
    enchanted: AttackTarget  # When set to `attacker`, this effect only works on enchanted weapon, regardless of the `slots` field.
    affected: AttackTarget
