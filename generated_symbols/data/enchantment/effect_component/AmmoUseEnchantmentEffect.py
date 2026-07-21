# Generated from symbols.json for ::java::data::enchantment::effect_component::AmmoUseEnchantmentEffect
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.effect.ValueEffect import ValueEffect
    from generated_symbols.data.predicate.Predicate import Predicate


@dataclass(kw_only=True)
class AmmoUseEnchantmentEffect:
    effect: ValueEffect  # Amount of ammunition being used up.  `0` has a side effect of applying `intangible_projectile` component to the projectile item.
    requirements: Predicate | None = None  # Predicate context: Item Parameters.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect_component::AmmoUseEnchantmentEffect": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Predicate context: Item Parameters.",
                "key": "requirements",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::predicate::Predicate"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Amount of ammunition being used up. \\\n`0` has a side effect of applying `intangible_projectile` component to the projectile item.",
                "key": "effect",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::effect::ValueEffect"
                }
            }
        ]
    }
}

