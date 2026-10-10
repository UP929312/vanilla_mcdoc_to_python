"""
Generated from symbols.json for ::java::data::recipe::CraftingImbue
Local link to file: vanilla_mcdoc/data/recipe/CraftingImbue.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.data.recipe.CraftingBookInfo import CraftingBookInfo
from vanilla_mcdoc.data.recipe.NotificationInfo import NotificationInfo

if TYPE_CHECKING:
    from vanilla_mcdoc.data.recipe.Ingredient import Ingredient
    from vanilla_mcdoc.world.item.ItemStackTemplate import ItemStackTemplate


class CraftingImbue(CraftingBookInfo, NotificationInfo):
    __resource_dir__: ClassVar[str] = 'recipe'

    source: Ingredient  # The item to provide potion effect.  Its `potion_contents` component will be copied.  This item is placed at the center grid.
    material: Ingredient  # Additional ingredients.  8 `material` items are required to surroud the `source` item.
    result: ItemStackTemplate
