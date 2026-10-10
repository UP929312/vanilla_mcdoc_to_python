"""
Generated from symbols.json for ::java::data::enchantment::effect::ChangeItemDamageEffect
Local link to file: vanilla_mcdoc/data/enchantment/effect/ChangeItemDamageEffect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.enchantment.LevelBasedValue import LevelBasedValue


class ChangeItemDamageEffect(GeneratedModel):
    amount: LevelBasedValue  # Damage to apply to the enchanted item. Negative values will repair the item. The change is not applied to items held by players in creative mode.
