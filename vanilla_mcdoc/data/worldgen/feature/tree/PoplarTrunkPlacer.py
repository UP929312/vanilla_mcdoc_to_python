"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::PoplarTrunkPlacer
Local link to file: vanilla_mcdoc/data/worldgen/feature/tree/PoplarTrunkPlacer.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.IntProvider import IntProvider


class PoplarTrunkPlacer(GeneratedModel):
    trunk_height_above_branches: IntProvider[Annotated[int, Field(ge=0, le=8)]] | Annotated[int, Field(ge=0, le=8)]
    branch_amount: IntProvider[Annotated[int, Field(ge=1, le=4)]] | Annotated[int, Field(ge=1, le=4)]
