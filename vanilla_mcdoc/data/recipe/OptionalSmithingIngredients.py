"""
Generated from symbols.json for ::java::data::recipe::OptionalSmithingIngredients
Local link to file: vanilla_mcdoc/data/recipe/OptionalSmithingIngredients.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.recipe.Ingredient import Ingredient


class OptionalSmithingIngredients(GeneratedModel):
    base: Ingredient | None = None  # Ingredient specifying an item to be trimmed. (eg. `"#minecraft:trimmable_armor"`)
    addition: Ingredient | None = None  # Material that will be used. (eg. `"#minecraft:trim_materials"`)
    template: Ingredient | None = None  # Template item that will be used for the pattern.
