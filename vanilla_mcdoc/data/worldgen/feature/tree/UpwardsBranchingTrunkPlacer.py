"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::UpwardsBranchingTrunkPlacer
Local link to file: vanilla_mcdoc/data/worldgen/feature/tree/UpwardsBranchingTrunkPlacer.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.IntProvider import IntProvider
    from vanilla_mcdoc.registry.KnownBlockId import KnownBlockId


class UpwardsBranchingTrunkPlacer(GeneratedModel):
    extra_branch_steps: IntProvider[Annotated[int, Field(ge=1)]] | Annotated[int, Field(ge=1)]
    extra_branch_length: IntProvider[Annotated[int, Field(ge=0)]] | Annotated[int, Field(ge=0)]
    place_branch_per_log_probability: Annotated[float, Field(ge=0, le=1)]
    can_grow_through: list[Annotated[str, IdSpec(registry='block')] | KnownBlockId] | Annotated[str, IdSpec(registry='block', tags='allowed')] | KnownBlockId
