"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::CherryFoliagePlacer
Local link to file: vanilla_mcdoc/data/worldgen/feature/tree/CherryFoliagePlacer.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.IntProvider import IntProvider


class CherryFoliagePlacer(GeneratedModel):
    height: IntProvider[Annotated[int, Field(ge=4, le=16)]] | Annotated[int, Field(ge=4, le=16)]
    wide_bottom_layer_hole_chance: Annotated[float, Field(ge=0, le=1)]
    corner_hole_chance: Annotated[float, Field(ge=0, le=1)]
    hanging_leaves_chance: Annotated[float, Field(ge=0, le=1)]
    hanging_leaves_extension_chance: Annotated[float, Field(ge=0, le=1)]
