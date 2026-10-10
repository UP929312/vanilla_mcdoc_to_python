"""
Generated from symbols.json for ::java::data::enchantment::effect_component::SmashDamagePerBlockFallenEnchantmentEffect
Local link to file: vanilla_mcdoc/data/enchantment/effect_component/SmashDamagePerBlockFallenEnchantmentEffect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.enchantment.effect.ValueEffect import ValueEffect
    from vanilla_mcdoc.data.predicate.Predicate import Predicate


class SmashDamagePerBlockFallenEnchantmentEffect(GeneratedModel):
    requirements: Predicate | None = None  # Predicate context: Damage Parameters.
    effect: ValueEffect  # Amount of damage dealt per block fallen.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect_component::SmashDamagePerBlockFallenEnchantmentEffect": {
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
                "desc": "Amount of damage dealt per block fallen.",
                "key": "effect",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::effect::ValueEffect"
                }
            }
        ]
    }
}
