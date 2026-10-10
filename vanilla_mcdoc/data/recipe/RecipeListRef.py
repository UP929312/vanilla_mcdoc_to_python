"""
Generated from symbols.json for ::java::data::recipe::RecipeListRef
Local link to file: vanilla_mcdoc/data/recipe/RecipeListRef.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.minecraft_types import IdSpec


type RecipeListRef = Annotated[str, IdSpec(registry='recipe', tags='allowed')] | list[Annotated[str, IdSpec(registry='recipe')]]
