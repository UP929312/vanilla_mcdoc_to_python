# Generated from symbols.json for ::java::data::enchantment::effect_component::ProjectileSpawnedEnchantmentEffect
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.effect.EntityEffect import EntityEffect
    from generated_symbols.data.predicate.Predicate import Predicate


@dataclass(kw_only=True)
class ProjectileSpawnedEnchantmentEffect:
    effect: EntityEffect  # On the newly spawned projectile.
    requirements: Predicate | None = None  # Predicate context: Entity Parameters.  `this` is the newly spawned projectile.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect_component::ProjectileSpawnedEnchantmentEffect": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Predicate context: Entity Parameters.\n\n`this` is the newly spawned projectile.",
                "key": "requirements",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::predicate::Predicate"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "On the newly spawned projectile.",
                "key": "effect",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::effect::EntityEffect"
                }
            }
        ]
    }
}

