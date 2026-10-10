"""
Generated from symbols.json for ::java::data::recipe::CraftingShaped
Local link to file: vanilla_mcdoc/data/recipe/CraftingShaped.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from vanilla_mcdoc.data.recipe.CraftingBookInfo import CraftingBookInfo
from vanilla_mcdoc.data.recipe.NotificationInfo import NotificationInfo

if TYPE_CHECKING:
    from vanilla_mcdoc.data.recipe.Ingredient import Ingredient
    from vanilla_mcdoc.world.item.ItemStackTemplate import ItemStackTemplate


class CraftingShaped(CraftingBookInfo, NotificationInfo):
    __resource_dir__: ClassVar[str] = 'recipe'

    pattern: Annotated[list[Annotated[str, Field(min_length=1, max_length=3)]], Field(min_length=1, max_length=3)]
    key: dict[str, Ingredient]
    result: ItemStackTemplate
