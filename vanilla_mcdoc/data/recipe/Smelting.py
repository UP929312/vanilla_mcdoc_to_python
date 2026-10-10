"""
Generated from symbols.json for ::java::data::recipe::Smelting
Local link to file: vanilla_mcdoc/data/recipe/Smelting.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.data.recipe.CookingBookInfo import CookingBookInfo
from vanilla_mcdoc.data.recipe.NotificationInfo import NotificationInfo

if TYPE_CHECKING:
    from vanilla_mcdoc.data.recipe.Ingredient import Ingredient
    from vanilla_mcdoc.world.item.ItemStackTemplate import ItemStackTemplate


class Smelting(CookingBookInfo, NotificationInfo):
    __resource_dir__: ClassVar[str] = 'recipe'

    ingredient: Ingredient
    result: ItemStackTemplate
    experience: float | None = None
    cookingtime: int  # Hint: The "Normal" value for this is `200`.
