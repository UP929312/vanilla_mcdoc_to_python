"""
Generated from symbols.json for ::java::data::enchantment::effect_component::AmmoUseEnchantmentEffect
Local link to file: vanilla_mcdoc/data/enchantment/effect_component/AmmoUseEnchantmentEffect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.enchantment.effect.ValueEffect import ValueEffect
    from vanilla_mcdoc.data.predicate.Predicate import Predicate


class AmmoUseEnchantmentEffect(GeneratedModel):
    requirements: Predicate | None = None  # Predicate context: Item Parameters.
    effect: ValueEffect  # Amount of ammunition being used up.  `0` has a side effect of applying `intangible_projectile` component to the projectile item.


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
