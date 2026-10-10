"""
Generated from symbols.json for ::java::data::recipe::SmithingTransform
Local link to file: vanilla_mcdoc/data/recipe/SmithingTransform.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.data.recipe.NotificationInfo import NotificationInfo

if TYPE_CHECKING:
    from vanilla_mcdoc.data.recipe.Ingredient import Ingredient
    from vanilla_mcdoc.world.item.ItemStackTemplate import ItemStackTemplate


class SmithingTransform(NotificationInfo):
    __resource_dir__: ClassVar[str] = 'recipe'

    base: Ingredient  # Ingredient specifying an item to be transformed.
    addition: Ingredient | None = None  # Material that will be used.
    template: Ingredient | None = None  # Template item that will be used for the pattern.
    result: ItemStackTemplate  # Resulting transformed item.
