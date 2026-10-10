"""
Generated from symbols.json for ::java::data::enchantment::effect_component::EquipmentDropsEnchantmentEffect
Local link to file: vanilla_mcdoc/data/enchantment/effect_component/EquipmentDropsEnchantmentEffect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Literal

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.enchantment.effect.ValueEffect import ValueEffect
    from vanilla_mcdoc.data.predicate.Predicate import Predicate


class EquipmentDropsEnchantmentEffect(GeneratedModel):
    requirements: Predicate | None = None  # Predicate context: Damage Parameters.
    effect: ValueEffect  # Chance between `0.0` and `1.0` of an equipped piece dropping.  If the drop chance on mob is 0, the chance will not be affected by this effect.
    enchanted: Literal['attacker'] | Literal['victim']  # Which subject needs to be enchanted for the effect to apply.
