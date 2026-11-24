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
    custom_name: str | None = None  # Overrides item name of potion, splash potion, lingering potion and tipped arrow.  The first present value is used as `<name>` to generate the translation key `item.minecraft.<item_id>.effect.<name>`: 1. This field 2. The default name provided by the `potion` type. 3. Literal `empty`.
    custom_effects: list[MobEffectInstance] | None = None
