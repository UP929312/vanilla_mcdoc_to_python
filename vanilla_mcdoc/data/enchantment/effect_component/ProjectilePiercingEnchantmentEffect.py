"""
Generated from symbols.json for ::java::data::enchantment::effect_component::ProjectilePiercingEnchantmentEffect
Local link to file: vanilla_mcdoc/data/enchantment/effect_component/ProjectilePiercingEnchantmentEffect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.enchantment.effect.ValueEffect import ValueEffect
    from vanilla_mcdoc.data.predicate.Predicate import Predicate


class ProjectilePiercingEnchantmentEffect(GeneratedModel):
    requirements: Predicate | None = None  # Predicate context: Item Parameters.  Tool is the ammunition item.
    effect: ValueEffect  # Amount of entities the projectile will pierce through before despawning.
