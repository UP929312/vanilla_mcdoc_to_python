"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::CherryTrunkPlacer
Local link to file: vanilla_mcdoc/data/worldgen/feature/tree/CherryTrunkPlacer.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.IntProvider import IntProvider
    from vanilla_mcdoc.data.worldgen.UniformIntProvider import UniformIntProvider


class CherryTrunkPlacer(GeneratedModel):
    branch_count: IntProvider[Annotated[int, Field(ge=1, le=3)]] | Annotated[int, Field(ge=1, le=3)]
    branch_horizontal_length: IntProvider[Annotated[int, Field(ge=2, le=16)]] | Annotated[int, Field(ge=2, le=16)]
    branch_start_offset_from_top: UniformIntProvider[Annotated[int, Field(ge=-16, le=0)]] | Annotated[int, Field(ge=-16, le=0)]
    branch_end_offset_from_top: IntProvider[Annotated[int, Field(ge=-16, le=16)]] | Annotated[int, Field(ge=-16, le=16)]
