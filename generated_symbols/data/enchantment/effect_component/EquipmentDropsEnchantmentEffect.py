# Generated from symbols.json for ::java::data::enchantment::effect_component::EquipmentDropsEnchantmentEffect
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.effect.ValueEffect import ValueEffect
    from generated_symbols.data.predicate.Predicate import Predicate


@dataclass(kw_only=True)
class EquipmentDropsEnchantmentEffect:
    effect: ValueEffect  # Chance between `0.0` and `1.0` of an equipped piece dropping.  If the drop chance on mob is 0, the chance will not be affected by this effect.
    enchanted: str  # Which subject needs to be enchanted for the effect to apply.
    requirements: Predicate | None = None  # Predicate context: Damage Parameters.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect_component::EquipmentDropsEnchantmentEffect": {
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
                "desc": "Chance between `0.0` and `1.0` of an equipped piece dropping. \\\nIf the drop chance on mob is 0, the chance will not be affected by this effect.",
                "key": "effect",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::effect::ValueEffect"
                }
            },
            {
                "kind": "pair",
                "desc": "Which subject needs to be enchanted for the effect to apply.",
                "key": "enchanted",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "attacker"
                            }
                        },
                        {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "victim"
                            }
                        }
                    ]
                }
            }
        ]
    }
}

