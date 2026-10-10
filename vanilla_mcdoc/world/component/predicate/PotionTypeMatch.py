"""
Generated from symbols.json for ::java::world::component::predicate::PotionTypeMatch
Local link to file: vanilla_mcdoc/world/component/predicate/PotionTypeMatch.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.minecraft_types import IdSpec


type PotionTypeMatch = Annotated[str, IdSpec(registry='potion', tags='allowed')] | list[Annotated[str, IdSpec(registry='potion')]]
