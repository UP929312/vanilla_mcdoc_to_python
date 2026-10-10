# ~~~ WHAT ARE WE TESTING ~~~

# Pair unions materialize nested structs in source order instead of emitting their keys as types.

# ~~~ FILE CONTENT ~~~
"""
Generated from symbols.json for ::java::data::worldgen::structure::TrickyTrialsStructureConfig
Local link to file: vanilla_mcdoc/data/worldgen/structure/TrickyTrialsStructureConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.structure.LiquidSettings import LiquidSettings


class DimensionPaddingStruct(GeneratedModel):
    bottom: Annotated[int, Field(ge=0)] | None = None
    top: Annotated[int, Field(ge=0)] | None = None


class TrickyTrialsStructureConfig(GeneratedModel):
    dimension_padding: Annotated[int, Field(ge=0)] | DimensionPaddingStruct | None = None
    liquid_settings: LiquidSettings | None = None
