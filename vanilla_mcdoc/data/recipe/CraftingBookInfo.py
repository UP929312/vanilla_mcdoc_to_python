"""
Generated from symbols.json for ::java::data::recipe::CraftingBookInfo
Local link to file: vanilla_mcdoc/data/recipe/CraftingBookInfo.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.recipe.CraftingBookCategory import CraftingBookCategory


class CraftingBookInfo(GeneratedModel):
    group: str | None = None  # Identifier to group multiple recipes in the recipe book.
    category: CraftingBookCategory | None = None  # Identifier for the category this goes in the recipe book.
