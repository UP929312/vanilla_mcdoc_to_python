"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::BendingTrunkPlacer
Local link to file: vanilla_mcdoc/data/worldgen/feature/tree/BendingTrunkPlacer.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.IntProvider import IntProvider


class BendingTrunkPlacer(GeneratedModel):
    bend_length: IntProvider[Annotated[int, Field(ge=1, le=64)]] | Annotated[int, Field(ge=1, le=64)]
    min_height_for_leaves: Annotated[int, Field(ge=1)] | None = None
