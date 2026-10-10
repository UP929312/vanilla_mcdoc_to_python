"""
Generated from symbols.json for ::java::data::recipe::CraftingSpecialBannerDuplicate
Local link to file: vanilla_mcdoc/data/recipe/CraftingSpecialBannerDuplicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.recipe.Ingredient import Ingredient
    from vanilla_mcdoc.world.item.ItemStackTemplate import ItemStackTemplate


class CraftingSpecialBannerDuplicate(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'recipe'

    banner: Ingredient  # The banner item. The item type is required to be `BannerItem`.  Exactly 2 banners of the same color are required.  The one with patterns is viewed as "source". Its components will be copied.  The other is viewed as "target". It is required to have no patterns.   The source banner will be kept in the crafting grid.
    result: ItemStackTemplate
