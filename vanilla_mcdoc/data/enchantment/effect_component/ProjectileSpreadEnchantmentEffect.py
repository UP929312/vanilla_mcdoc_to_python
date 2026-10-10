"""
Generated from symbols.json for ::java::data::enchantment::effect_component::ProjectileSpreadEnchantmentEffect
Local link to file: vanilla_mcdoc/data/enchantment/effect_component/ProjectileSpreadEnchantmentEffect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.enchantment.effect.ValueEffect import ValueEffect
    from vanilla_mcdoc.data.predicate.Predicate import Predicate


class ProjectileSpreadEnchantmentEffect(GeneratedModel):
    requirements: Predicate | None = None  # Predicate context: Entity Parameters.  `this` is the entity shooting the projectile.
    effect: ValueEffect  # Maximum spread of projectiles measured in degrees from the aim line.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect_component::ProjectileSpreadEnchantmentEffect": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Predicate context: Entity Parameters.\n\n`this` is the entity shooting the projectile.",
                "key": "requirements",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::predicate::Predicate"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Maximum spread of projectiles measured in degrees from the aim line.",
                "key": "effect",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::effect::ValueEffect"
                }
            }
        ]
    }
}
