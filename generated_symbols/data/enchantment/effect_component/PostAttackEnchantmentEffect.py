# Generated from symbols.json for ::java::data::enchantment::effect_component::PostAttackEnchantmentEffect
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.effect.EntityEffect import EntityEffect
    from generated_symbols.data.enchantment.effect_component.AttackTarget import AttackTarget
    from generated_symbols.data.predicate.Predicate import Predicate


@dataclass(kw_only=True)
class PostAttackEnchantmentEffect:
    effect: EntityEffect  # Examples: - A Fire Aspect Enchant would specify that when the attacker is enchanted, the `ignite` effect is applied, and the affected party is the victim. - Thorns would specify that when the victim is enchanted, the `damage_entity` effect is applied, and the affected party is the attacker.
    enchanted: AttackTarget  # When set to `attacker`, this effect only works on enchanted weapon, regardless of the `slots` field.
    affected: AttackTarget
    requirements: Predicate | None = None  # Predicate context: Damage Parameters.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect_component::PostAttackEnchantmentEffect": {
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
                "desc": "Examples:\n- A Fire Aspect Enchant would specify that when the attacker is enchanted, the `ignite` effect is applied, and the affected party is the victim.\n- Thorns would specify that when the victim is enchanted, the `damage_entity` effect is applied, and the affected party is the attacker.",
                "key": "effect",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::effect::EntityEffect"
                }
            },
            {
                "kind": "pair",
                "desc": "When set to `attacker`, this effect only works on enchanted weapon, regardless of the `slots` field.",
                "key": "enchanted",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::effect_component::AttackTarget"
                }
            },
            {
                "kind": "pair",
                "key": "affected",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::effect_component::AttackTarget"
                }
            }
        ]
    }
}

