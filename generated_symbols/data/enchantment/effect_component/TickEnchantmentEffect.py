# Generated from symbols.json for ::java::data::enchantment::effect_component::TickEnchantmentEffect
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.effect.EntityEffect import EntityEffect
    from generated_symbols.data.predicate.Predicate import Predicate


@dataclass(kw_only=True)
class TickEnchantmentEffect:
    effect: EntityEffect  # On every tick. Performance recommendation: don't use with `run_function` unless necessary.
    requirements: Predicate | None = None  # Predicate context: Entity Parameters.  `this` is the entity with the Enchanted Item.


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

