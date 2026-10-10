"""
Generated from symbols.json for ::java::data::worldgen::structure_set::ExclusionZone
Local link to file: vanilla_mcdoc/data/worldgen/structure_set/ExclusionZone.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.structure_set.StructureSetRef import StructureSetRef


class ExclusionZone(GeneratedModel):
    other_set: StructureSetRef
    chunk_count: Annotated[int, Field(ge=1, le=16)]
