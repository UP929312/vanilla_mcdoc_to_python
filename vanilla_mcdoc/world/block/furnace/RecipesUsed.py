"""
Generated from symbols.json for ::java::world::block::furnace::RecipesUsed
Local link to file: vanilla_mcdoc/world/block/furnace/RecipesUsed.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.minecraft_types import IdSpec


type RecipesUsed = dict[Annotated[str, IdSpec(registry='recipe')], int]
