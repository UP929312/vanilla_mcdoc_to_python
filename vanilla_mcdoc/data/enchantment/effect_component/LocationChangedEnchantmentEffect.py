"""
Generated from symbols.json for ::java::data::enchantment::effect_component::LocationChangedEnchantmentEffect
Local link to file: vanilla_mcdoc/data/enchantment/effect_component/LocationChangedEnchantmentEffect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.enchantment.effect.LocationBasedEffect import LocationBasedEffect
    from vanilla_mcdoc.data.predicate.Predicate import Predicate


class LocationChangedEnchantmentEffect(GeneratedModel):
    requirements: Predicate | None = None  # Predicate context: Location Parameters.
    effect: LocationBasedEffect  # On the entity changing location.
