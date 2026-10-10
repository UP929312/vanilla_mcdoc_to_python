"""
Generated from symbols.json for ::java::data::recipe::SmithingTrim
Local link to file: vanilla_mcdoc/data/recipe/SmithingTrim.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from vanilla_mcdoc.data.recipe.NotificationInfo import NotificationInfo
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.recipe.Ingredient import Ingredient


class SmithingTrim(NotificationInfo):
    __resource_dir__: ClassVar[str] = 'recipe'

    base: Ingredient  # Ingredient specifying an item to be trimmed.
    addition: Ingredient  # Material that will be used.
    template: Ingredient  # Template item that will be used for the pattern.
    pattern: Annotated[str, IdSpec(registry='trim_pattern')]  # The trim pattern to apply to the result item.
