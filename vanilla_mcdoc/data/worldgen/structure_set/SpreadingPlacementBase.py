"""
Generated from symbols.json for ::java::data::worldgen::structure_set::SpreadingPlacementBase
Local link to file: vanilla_mcdoc/data/worldgen/structure_set/SpreadingPlacementBase.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.structure_set.ExclusionZone import ExclusionZone
    from vanilla_mcdoc.data.worldgen.structure_set.FrequencyReductionMethod import FrequencyReductionMethod


class SpreadingPlacementBase(GeneratedModel):
    salt: Annotated[int, Field(ge=0)]
    frequency_reduction_method: FrequencyReductionMethod | None = None
    frequency: Annotated[float, Field(ge=0, le=1)] | None = None
    exclusion_zone: ExclusionZone | None = None
    locate_offset: tuple[Annotated[int, Field(ge=-16, le=16)], Annotated[int, Field(ge=-16, le=16)], Annotated[int, Field(ge=-16, le=16)]] | None = None
