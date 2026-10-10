"""
Generated from symbols.json for ::java::data::enchantment::effect_component::ArmorEffectivenessEnchantmentEffect
Local link to file: vanilla_mcdoc/data/enchantment/effect_component/ArmorEffectivenessEnchantmentEffect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.enchantment.effect.ValueEffect import ValueEffect
    from vanilla_mcdoc.data.predicate.Predicate import Predicate


class ArmorEffectivenessEnchantmentEffect(GeneratedModel):
    requirements: Predicate | None = None  # Predicate context: Damage Parameters.
    effect: ValueEffect  # Determines armor effectiveness; `0.0` for no effect, `1.0` for full effect.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect_component::ArmorEffectivenessEnchantmentEffect": {
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
                "desc": "Determines armor effectiveness; `0.0` for no effect, `1.0` for full effect.",
                "key": "effect",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::effect::ValueEffect"
                }
            }
        ]
    }
}
