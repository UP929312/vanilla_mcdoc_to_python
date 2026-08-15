"""
Generated from symbols.json for ::java::data::enchantment::effect_component::TridentReturnAccelerationEnchantmentEffect
Local link to file: generated_symbols/data/enchantment/effect_component/TridentReturnAccelerationEnchantmentEffect.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.effect.ValueEffect import ValueEffect
    from generated_symbols.data.predicate.Predicate import Predicate


@dataclass(kw_only=True)
class TridentReturnAccelerationEnchantmentEffect:
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

