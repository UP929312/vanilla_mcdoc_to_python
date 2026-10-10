"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::PoplarFoliagePlacer
Local link to file: vanilla_mcdoc/data/worldgen/feature/tree/PoplarFoliagePlacer.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.IntProvider import IntProvider


class PoplarFoliagePlacer(GeneratedModel):
    height: IntProvider[Annotated[int, Field(ge=5, le=16)]] | Annotated[int, Field(ge=5, le=16)]
    side_hole_chance: Annotated[float, Field(ge=0, le=1)]
