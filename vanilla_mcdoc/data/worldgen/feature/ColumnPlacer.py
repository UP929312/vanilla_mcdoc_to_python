"""
Generated from symbols.json for ::java::data::worldgen::feature::ColumnPlacer
Local link to file: vanilla_mcdoc/data/worldgen/feature/ColumnPlacer.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.IntProvider import IntProvider


class ColumnPlacer(GeneratedModel):
    size: IntProvider[Annotated[int, Field(ge=0)]] | Annotated[int, Field(ge=0)]
