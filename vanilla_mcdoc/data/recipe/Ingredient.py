"""
Generated from symbols.json for ::java::data::recipe::Ingredient
Local link to file: vanilla_mcdoc/data/recipe/Ingredient.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.minecraft_types import IdSpec


type Ingredient = Annotated[list[Annotated[str, IdSpec(registry='item', exclude=('air',))]], Field(min_length=1)] | Annotated[str, IdSpec(registry='item', tags='allowed', exclude=('air',))]
