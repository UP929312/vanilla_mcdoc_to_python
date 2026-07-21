# Generated from symbols.json for ::java::data::enchantment::effect_component::PostPiercingAttackEnchantmentEffect
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.effect.EntityEffect import EntityEffect
    from generated_symbols.data.predicate.Predicate import Predicate


@dataclass(kw_only=True)
class PostPiercingAttackEnchantmentEffect:
    effect: EntityEffect  # The effect to apply on attacker.
    requirements: Predicate | None = None  # Predicate context: Damage Parameters.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect_component::PostPiercingAttackEnchantmentEffect": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Predicate context: Damage Parameters.",
                "key": "requirements",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::predicate::Predicate"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "The effect to apply on attacker.",
                "key": "effect",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::effect::EntityEffect"
                }
            }
        ]
    }
}

