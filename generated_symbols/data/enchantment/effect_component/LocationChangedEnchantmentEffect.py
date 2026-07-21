# Generated from symbols.json for ::java::data::enchantment::effect_component::LocationChangedEnchantmentEffect
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.effect.LocationBasedEffect import LocationBasedEffect
    from generated_symbols.data.predicate.Predicate import Predicate


@dataclass(kw_only=True)
class LocationChangedEnchantmentEffect:
    effect: LocationBasedEffect  # On the entity changing location.
    requirements: Predicate | None = None  # Predicate context: Location Parameters.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect_component::LocationChangedEnchantmentEffect": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Predicate context: Location Parameters.",
                "key": "requirements",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::predicate::Predicate"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "On the entity changing location.",
                "key": "effect",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::effect::LocationBasedEffect"
                }
            }
        ]
    }
}

