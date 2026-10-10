"""
Generated from symbols.json for ::java::data::advancement::predicate::PlayerRecipes
Local link to file: vanilla_mcdoc/data/advancement/predicate/PlayerRecipes.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.minecraft_types import IdSpec


type PlayerRecipes = dict[Annotated[str, IdSpec(registry='recipe')], bool]
