"""
Generated from symbols.json for ::java::data::enchantment::effect_component::RepairWithXpEnchantmentEffect
Local link to file: vanilla_mcdoc/data/enchantment/effect_component/RepairWithXpEnchantmentEffect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.enchantment.effect.ValueEffect import ValueEffect
    from vanilla_mcdoc.data.predicate.Predicate import Predicate


class RepairWithXpEnchantmentEffect(GeneratedModel):
    requirements: Predicate | None = None  # Predicate context: Item Parameters.
    effect: ValueEffect  # Amount of durability increase per experience point, `mending` uses 2x.
