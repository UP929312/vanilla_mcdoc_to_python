"""
Generated from symbols.json for ::java::data::enchantment::effect_component::ItemDamageEnchantmentEffect
Local link to file: vanilla_mcdoc/data/enchantment/effect_component/ItemDamageEnchantmentEffect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.enchantment.effect.ValueEffect import ValueEffect
    from vanilla_mcdoc.data.predicate.Predicate import Predicate


class ItemDamageEnchantmentEffect(GeneratedModel):
    requirements: Predicate | None = None  # Predicate context: Item Parameters.
    effect: ValueEffect  # Amount of damage being dealt to the item.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect_component::ItemDamageEnchantmentEffect": {
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
                "desc": "Amount of damage being dealt to the item.",
                "key": "effect",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::effect::ValueEffect"
                }
            }
        ]
    }
}
