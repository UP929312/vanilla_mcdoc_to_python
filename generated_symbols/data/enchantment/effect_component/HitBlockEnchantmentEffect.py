# Generated from symbols.json for ::java::data::enchantment::effect_component::HitBlockEnchantmentEffect
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.effect.EntityEffect import EntityEffect
    from generated_symbols.data.predicate.Predicate import Predicate


@dataclass(kw_only=True)
class HitBlockEnchantmentEffect:
    effect: EntityEffect  # On the entity hitting the Block
    requirements: Predicate | None = None  # Predicate context: Entity Parameters.  `this` is the entity hitting the Block, unless during a projectile attack, then, `this` is the projectile.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect_component::HitBlockEnchantmentEffect": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Predicate context: Entity Parameters.\n\n`this` is the entity hitting the Block, unless during a projectile attack, then, `this` is the projectile.",
                "key": "requirements",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::predicate::Predicate"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "On the entity hitting the Block",
                "key": "effect",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::effect::EntityEffect"
                }
            }
        ]
    }
}

