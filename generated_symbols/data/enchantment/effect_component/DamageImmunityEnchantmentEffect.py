# Generated from symbols.json for ::java::data::enchantment::effect_component::DamageImmunityEnchantmentEffect
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from generated_symbols.data.predicate.Predicate import Predicate


@dataclass(kw_only=True)
class DamageImmunityEnchantmentEffect:
    effect: Any  # Dummy value; this is a boolean effect.
    requirements: Predicate | None = None  # Predicate context: Damage Parameters.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect_component::DamageImmunityEnchantmentEffect": {
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
                "desc": "Dummy value; this is a boolean effect.",
                "key": "effect",
                "type": {
                    "kind": "struct",
                    "fields": []
                }
            }
        ]
    }
}

