"""
Generated from symbols.json for ::java::data::enchantment::effect_component::PostPiercingAttackEnchantmentEffect
Local link to file: vanilla_mcdoc/data/enchantment/effect_component/PostPiercingAttackEnchantmentEffect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.enchantment.effect.EntityEffect import EntityEffect
    from vanilla_mcdoc.data.predicate.Predicate import Predicate


class PostPiercingAttackEnchantmentEffect(GeneratedModel):
    requirements: Predicate | None = None  # Predicate context: Damage Parameters.
    effect: EntityEffect  # The effect to apply on attacker.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect_component::PostPiercingAttackEnchantmentEffect": {
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
                "desc": "The effect to apply on attacker.",
                "key": "effect",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::effect::EntityEffect"
                }
            }
        ]
    }
}
