"""
Generated from symbols.json for ::java::data::recipe::Stonecutting
Local link to file: vanilla_mcdoc/data/recipe/Stonecutting.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.data.recipe.NotificationInfo import NotificationInfo

if TYPE_CHECKING:
    from vanilla_mcdoc.data.recipe.Ingredient import Ingredient
    from vanilla_mcdoc.world.item.ItemStackTemplate import ItemStackTemplate


class Stonecutting(NotificationInfo):
    __resource_dir__: ClassVar[str] = 'recipe'

    ingredient: Ingredient
    result: ItemStackTemplate
