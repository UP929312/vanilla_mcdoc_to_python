# ~~~ WHAT ARE WE TESTING ~~~

# Pair unions materialize nested structs in source order instead of emitting their keys as types.

# ~~~ FILE CONTENT ~~~
"""
Generated from symbols.json for ::java::data::worldgen::structure::TrickyTrialsStructureConfig
Local link to file: generated_symbols/data/worldgen/structure/TrickyTrialsStructureConfig.py
"""
# ~~~ CODE ~~~
from pydantic import BaseModel
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.structure.LiquidSettings import LiquidSettings


class DimensionPaddingStruct(BaseModel):
    bottom: Annotated[int, 'Range | `0` and above | inclusive'] | None = None
    top: Annotated[int, 'Range | `0` and above | inclusive'] | None = None


class TrickyTrialsStructureConfig(BaseModel):
    dimension_padding: Annotated[int, 'Range | `0` and above | inclusive'] | DimensionPaddingStruct | None = None
    liquid_settings: LiquidSettings | None = None


