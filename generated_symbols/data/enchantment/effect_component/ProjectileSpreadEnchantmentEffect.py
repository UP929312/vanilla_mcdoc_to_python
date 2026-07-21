# Generated from symbols.json for ::java::data::enchantment::effect_component::ProjectileSpreadEnchantmentEffect
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.effect.ValueEffect import ValueEffect
    from generated_symbols.data.predicate.Predicate import Predicate


@dataclass(kw_only=True)
class ProjectileSpreadEnchantmentEffect:
    effect: ValueEffect  # Maximum spread of projectiles measured in degrees from the aim line.
    requirements: Predicate | None = None  # Predicate context: Entity Parameters.  `this` is the entity shooting the projectile.


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

