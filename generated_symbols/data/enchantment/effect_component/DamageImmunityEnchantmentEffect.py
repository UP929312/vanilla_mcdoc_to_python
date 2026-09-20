"""
Generated from symbols.json for ::java::data::enchantment::effect_component::DamageImmunityEnchantmentEffect
Local link to file: generated_symbols/data/enchantment/effect_component/DamageImmunityEnchantmentEffect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.predicate.Predicate import Predicate


class EffectStruct(GeneratedModel):
    pass


class DamageImmunityEnchantmentEffect(GeneratedModel):
    requirements: Predicate | None = None  # Predicate context: Damage Parameters.
    effect: EffectStruct  # Dummy value; this is a boolean effect.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect_component::DamageImmunityEnchantmentEffect": {
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
                "desc": "Dummy value; this is a boolean effect.",
                "key": "effect",
                "type": {
                    "kind": "struct",
                    "fields": []
                }
            }
        ]
    }
}

