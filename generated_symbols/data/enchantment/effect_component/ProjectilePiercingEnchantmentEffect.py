# Generated from symbols.json for ::java::data::enchantment::effect_component::ProjectilePiercingEnchantmentEffect
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.effect.ValueEffect import ValueEffect
    from generated_symbols.data.predicate.Predicate import Predicate


@dataclass(kw_only=True)
class ProjectilePiercingEnchantmentEffect:
    effect: ValueEffect  # Amount of entities the projectile will pierce through before despawning.
    requirements: Predicate | None = None  # Predicate context: Item Parameters.  Tool is the ammunition item.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect_component::ProjectilePiercingEnchantmentEffect": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Predicate context: Item Parameters.\n\nTool is the ammunition item.",
                "key": "requirements",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::predicate::Predicate"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Amount of entities the projectile will pierce through before despawning.",
                "key": "effect",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::effect::ValueEffect"
                }
            }
        ]
    }
}

