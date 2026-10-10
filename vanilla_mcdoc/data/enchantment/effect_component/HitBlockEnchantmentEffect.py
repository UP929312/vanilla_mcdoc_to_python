"""
Generated from symbols.json for ::java::data::enchantment::effect_component::HitBlockEnchantmentEffect
Local link to file: vanilla_mcdoc/data/enchantment/effect_component/HitBlockEnchantmentEffect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.enchantment.effect.EntityEffect import EntityEffect
    from vanilla_mcdoc.data.predicate.Predicate import Predicate


class HitBlockEnchantmentEffect(GeneratedModel):
    requirements: Predicate | None = None  # Predicate context: Entity Parameters.  `this` is the entity hitting the Block, unless during a projectile attack, then, `this` is the projectile.
    effect: EntityEffect  # On the entity hitting the Block


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
