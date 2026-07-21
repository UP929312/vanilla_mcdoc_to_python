# Generated from symbols.json for ::java::data::enchantment::effect_component::ProjectileCountEnchantmentEffect
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.effect.ValueEffect import ValueEffect
    from generated_symbols.data.predicate.Predicate import Predicate


@dataclass(kw_only=True)
class ProjectileCountEnchantmentEffect:
    effect: ValueEffect  # Amount of projectiles being loaded/drawn.  All projectile items except the first one will have `intangible_projectile` component applied.
    requirements: Predicate | None = None  # Predicate context: Entity Parameters.  `this` is the entity drawing the weapon.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect_component::ProjectileCountEnchantmentEffect": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Predicate context: Entity Parameters.\n\n`this` is the entity drawing the weapon.",
                "key": "requirements",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::predicate::Predicate"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Amount of projectiles being loaded/drawn. \\\nAll projectile items except the first one will have `intangible_projectile` component applied.",
                "key": "effect",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::effect::ValueEffect"
                }
            }
        ]
    }
}

