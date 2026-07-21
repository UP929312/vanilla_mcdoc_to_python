# Generated from symbols.json for ::java::data::enchantment::effect_component::MobExperienceEnchantmentEffect
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.effect.ValueEffect import ValueEffect
    from generated_symbols.data.predicate.Predicate import Predicate


@dataclass(kw_only=True)
class MobExperienceEnchantmentEffect:
    effect: ValueEffect  # Amount of experience awarded.
    requirements: Predicate | None = None  # Predicate context: Entity Parameters.  `this` is the killed mob.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect_component::MobExperienceEnchantmentEffect": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Predicate context: Entity Parameters.\n\n`this` is the killed mob.",
                "key": "requirements",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::predicate::Predicate"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Amount of experience awarded.",
                "key": "effect",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::effect::ValueEffect"
                }
            }
        ]
    }
}

