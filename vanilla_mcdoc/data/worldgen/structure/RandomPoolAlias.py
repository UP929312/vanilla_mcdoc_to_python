"""
Generated from symbols.json for ::java::data::worldgen::structure::RandomPoolAlias
Local link to file: vanilla_mcdoc/data/worldgen/structure/RandomPoolAlias.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.util.NonEmptyWeightedList import NonEmptyWeightedList


class RandomPoolAlias(GeneratedModel):
    alias: Annotated[str, IdSpec()]
    targets: NonEmptyWeightedList[Annotated[str, IdSpec(registry='worldgen/template_pool')]]
