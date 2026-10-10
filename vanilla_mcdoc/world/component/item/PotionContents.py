"""
Generated from symbols.json for ::java::world::component::item::PotionContents
Local link to file: vanilla_mcdoc/world/component/item/PotionContents.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.util.effect.MobEffectInstance import MobEffectInstance


class PotionContents(GeneratedModel):
    potion: Annotated[str, IdSpec(registry='potion')] | None = None
    custom_color: int | None = None  # Calculated as `RED << 16 | GREEN << 8 | BLUE`. Each of these fields must be between 0 and 255, inclusive.
    custom_name: str | None = None  # If present, is used to generate the item name using the translation key `item.minecraft.<potion_type>.effect.<custom_name>`.
    custom_effects: list[MobEffectInstance] | None = None
