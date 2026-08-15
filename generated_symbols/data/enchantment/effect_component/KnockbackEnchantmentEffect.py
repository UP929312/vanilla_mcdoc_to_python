"""
Generated from symbols.json for ::java::data::enchantment::effect_component::KnockbackEnchantmentEffect
Local link to file: generated_symbols/data/enchantment/effect_component/KnockbackEnchantmentEffect.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.effect.ValueEffect import ValueEffect
    from generated_symbols.data.predicate.Predicate import Predicate


@dataclass(kw_only=True)
class KnockbackEnchantmentEffect:
    requirements: Predicate | None = None  # Predicate context: Damage Parameters.
    effect: ValueEffect  # Amount of knockback being applied.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect_component::KnockbackEnchantmentEffect": {
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
                "desc": "Amount of knockback being applied.",
                "key": "effect",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::effect::ValueEffect"
                }
            }
        ]
    }
}

