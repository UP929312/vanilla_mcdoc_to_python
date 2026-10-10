"""
Generated from symbols.json for ::java::data::recipe::CraftingDye
Local link to file: vanilla_mcdoc/data/recipe/CraftingDye.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.data.recipe.CraftingBookInfo import CraftingBookInfo
from vanilla_mcdoc.data.recipe.NotificationInfo import NotificationInfo

if TYPE_CHECKING:
    from vanilla_mcdoc.data.recipe.Ingredient import Ingredient
    from vanilla_mcdoc.world.item.ItemStackTemplate import ItemStackTemplate


class CraftingDye(CraftingBookInfo, NotificationInfo):
    __resource_dir__: ClassVar[str] = 'recipe'

    target: Ingredient  # The item to be dyed.  Its `dyed_color` component will be dyed. The other components are copied.
    dye: Ingredient  # The items to provide dye color.  Colors are provided by the `dye` component.  Multiple dyes can be used at the same time.
    result: ItemStackTemplate
