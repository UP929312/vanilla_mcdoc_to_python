"""
Generated from symbols.json for ::java::data::recipe::RequiredSmithingIngredients
Local link to file: vanilla_mcdoc/data/recipe/RequiredSmithingIngredients.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.recipe.Ingredient import Ingredient


class RequiredSmithingIngredients(GeneratedModel):
    base: Ingredient  # Ingredient specifying an item to be trimmed. (eg. `{ "tag": "minecraft:trimmable_armor" }`)
    addition: Ingredient  # Material that will be used. (eg. `{ "tag": "minecraft:trim_materials" }`)
    template: Ingredient  # Template item that will be used for the pattern.
