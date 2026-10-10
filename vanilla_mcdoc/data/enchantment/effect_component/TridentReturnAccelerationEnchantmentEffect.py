"""
Generated from symbols.json for ::java::data::enchantment::effect_component::TridentReturnAccelerationEnchantmentEffect
Local link to file: vanilla_mcdoc/data/enchantment/effect_component/TridentReturnAccelerationEnchantmentEffect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.enchantment.effect.ValueEffect import ValueEffect
    from vanilla_mcdoc.data.predicate.Predicate import Predicate


class TridentReturnAccelerationEnchantmentEffect(GeneratedModel):
    requirements: Predicate | None = None  # Predicate context: Entity Parameters.  `this` is the trident entity.
    effect: ValueEffect  # Amount of acceleration applied to the returning trident.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect_component::TridentReturnAccelerationEnchantmentEffect": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Predicate context: Entity Parameters.\n\n`this` is the trident entity.",
                "key": "requirements",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::predicate::Predicate"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Amount of acceleration applied to the returning trident.",
                "key": "effect",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::effect::ValueEffect"
                }
            }
        ]
    }
}
