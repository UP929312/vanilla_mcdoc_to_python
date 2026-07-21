# Generated from symbols.json for ::java::data::enchantment::effect_component::RepairWithXpEnchantmentEffect
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.effect.ValueEffect import ValueEffect
    from generated_symbols.data.predicate.Predicate import Predicate


@dataclass(kw_only=True)
class RepairWithXpEnchantmentEffect:
    effect: ValueEffect  # Amount of durability increase per experience point, `mending` uses 2x.
    requirements: Predicate | None = None  # Predicate context: Item Parameters.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect_component::RepairWithXpEnchantmentEffect": {
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
                "desc": "Amount of durability increase per experience point, `mending` uses 2x.",
                "key": "effect",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::effect::ValueEffect"
                }
            }
        ]
    }
}

