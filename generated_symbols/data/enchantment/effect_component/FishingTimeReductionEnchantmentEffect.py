# Generated from symbols.json for ::java::data::enchantment::effect_component::FishingTimeReductionEnchantmentEffect
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.effect.ValueEffect import ValueEffect
    from generated_symbols.data.predicate.Predicate import Predicate


@dataclass(kw_only=True)
class FishingTimeReductionEnchantmentEffect:
    effect: ValueEffect  # Time reduction in seconds (higher values mean less time until a fish bites).
    requirements: Predicate | None = None  # Predicate context: Entity Parameters.  `this` is the player fishing.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect_component::FishingTimeReductionEnchantmentEffect": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Predicate context: Entity Parameters.\n\n`this` is the player fishing.",
                "key": "requirements",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::predicate::Predicate"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Time reduction in seconds (higher values mean less time until a fish bites).",
                "key": "effect",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::effect::ValueEffect"
                }
            }
        ]
    }
}

