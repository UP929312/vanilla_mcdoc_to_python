# Generated from symbols.json for ::java::data::enchantment::effect_component::FishingLuckBonusEnchantmentEffect
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.effect.ValueEffect import ValueEffect
    from generated_symbols.data.predicate.Predicate import Predicate


@dataclass(kw_only=True)
class FishingLuckBonusEnchantmentEffect:
    effect: ValueEffect  # Amount of luck being added.
    requirements: Predicate | None = None  # Predicate context: Entity Parameters.  `this` is the player fishing.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect_component::FishingLuckBonusEnchantmentEffect": {
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
                "desc": "Amount of luck being added.",
                "key": "effect",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::effect::ValueEffect"
                }
            }
        ]
    }
}

