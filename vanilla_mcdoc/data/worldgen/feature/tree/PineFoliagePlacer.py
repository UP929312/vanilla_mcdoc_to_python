"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::PineFoliagePlacer
Local link to file: vanilla_mcdoc/data/worldgen/feature/tree/PineFoliagePlacer.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.IntProvider import IntProvider


class PineFoliagePlacer(GeneratedModel):
    height: IntProvider[Annotated[int, Field(ge=0, le=24)]] | Annotated[int, Field(ge=0, le=24)]
