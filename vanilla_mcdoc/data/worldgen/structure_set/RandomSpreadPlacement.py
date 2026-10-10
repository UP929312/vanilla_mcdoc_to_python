"""
Generated from symbols.json for ::java::data::worldgen::structure_set::RandomSpreadPlacement
Local link to file: vanilla_mcdoc/data/worldgen/structure_set/RandomSpreadPlacement.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.data.worldgen.structure_set.SpreadingPlacementBase import SpreadingPlacementBase

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.structure_set.SpreadType import SpreadType


class RandomSpreadPlacement(SpreadingPlacementBase):
    spacing: Annotated[int, Field(ge=0, le=4096)]  # Average distance in chunks between two structures of this type.
    separation: Annotated[int, Field(ge=0, le=4096)]  # Minimum distance in chunks between two structures of this type.
    spread_type: SpreadType | None = None
