"""
Generated from symbols.json for ::java::data::enchantment::effect_component::LocationChangedEnchantmentEffect
Local link to file: generated_symbols/data/enchantment/effect_component/LocationChangedEnchantmentEffect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.effect.LocationBasedEffect import LocationBasedEffect
    from generated_symbols.data.predicate.Predicate import Predicate


class LocationChangedEnchantmentEffect(GeneratedModel):
    requirements: Predicate | None = None  # Predicate context: Location Parameters.
    effect: LocationBasedEffect  # On the entity changing location.


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
