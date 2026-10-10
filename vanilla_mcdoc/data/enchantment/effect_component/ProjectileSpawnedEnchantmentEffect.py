"""
Generated from symbols.json for ::java::data::enchantment::effect_component::ProjectileSpawnedEnchantmentEffect
Local link to file: vanilla_mcdoc/data/enchantment/effect_component/ProjectileSpawnedEnchantmentEffect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.enchantment.effect.EntityEffect import EntityEffect
    from vanilla_mcdoc.data.predicate.Predicate import Predicate


class ProjectileSpawnedEnchantmentEffect(GeneratedModel):
    requirements: Predicate | None = None  # Predicate context: Entity Parameters.  `this` is the newly spawned projectile.
    effect: EntityEffect  # On the newly spawned projectile.
