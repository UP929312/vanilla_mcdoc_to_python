"""
Generated from symbols.json for ::java::data::enchantment::effect_component::TickEnchantmentEffect
Local link to file: vanilla_mcdoc/data/enchantment/effect_component/TickEnchantmentEffect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.enchantment.effect.EntityEffect import EntityEffect
    from vanilla_mcdoc.data.predicate.Predicate import Predicate


class TickEnchantmentEffect(GeneratedModel):
    requirements: Predicate | None = None  # Predicate context: Entity Parameters.  `this` is the entity with the Enchanted Item.
    effect: EntityEffect  # On every tick. Performance recommendation: don't use with `run_function` unless necessary.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect_component::TickEnchantmentEffect": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Predicate context: Entity Parameters.\n\n`this` is the entity with the Enchanted Item.",
                "key": "requirements",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::predicate::Predicate"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "On every tick. Performance recommendation: don't use with `run_function` unless necessary.",
                "key": "effect",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::effect::EntityEffect"
                }
            }
        ]
    }
}
