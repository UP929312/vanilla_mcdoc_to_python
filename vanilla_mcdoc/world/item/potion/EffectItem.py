"""
Generated from symbols.json for ::java::world::item::potion::EffectItem
Local link to file: vanilla_mcdoc/world/item/potion/EffectItem.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.minecraft_types import IdSpec
from vanilla_mcdoc.world.item.ItemBase import ItemBase

if TYPE_CHECKING:
    from vanilla_mcdoc.util.effect.MobEffectInstance import MobEffectInstance


class EffectItem(ItemBase):
    custom_potion_effects: list[MobEffectInstance] | None = None  # List of the effects that will be applied with this item.
    Potion: Annotated[str, IdSpec(registry='potion')] | None = None  # Default potion effect
    CustomPotionColor: int | None = None  # Calculated as `RED << 16 | GREEN << 8 | BLUE`. Each of these fields must be between 0 and 255, inclusive.
