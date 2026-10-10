"""
Generated from symbols.json for ::java::data::enchantment::effect_component::ProjectileCountEnchantmentEffect
Local link to file: vanilla_mcdoc/data/enchantment/effect_component/ProjectileCountEnchantmentEffect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.enchantment.effect.ValueEffect import ValueEffect
    from vanilla_mcdoc.data.predicate.Predicate import Predicate


class ProjectileCountEnchantmentEffect(GeneratedModel):
    requirements: Predicate | None = None  # Predicate context: Entity Parameters.  `this` is the entity drawing the weapon.
    effect: ValueEffect  # Amount of projectiles being loaded/drawn.  All projectile items except the first one will have `intangible_projectile` component applied.
