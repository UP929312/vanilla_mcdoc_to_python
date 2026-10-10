"""
Generated from symbols.json for ::java::data::worldgen::feature::RandomNeighborSpreadConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/RandomNeighborSpreadConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.IntProvider import IntProvider
    from vanilla_mcdoc.data.worldgen.feature.block_predicate.BlockPredicate import BlockPredicate
    from vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef import BlockStateProviderRef
    from vanilla_mcdoc.registry.KnownBlockId import KnownBlockId


class RandomNeighborSpreadConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    block: BlockStateProviderRef
    accepted_neighbors: Annotated[str, IdSpec(registry='block', tags='allowed')] | KnownBlockId | list[Annotated[str, IdSpec(registry='block')] | KnownBlockId]
    can_replace: BlockPredicate
    attempts: IntProvider[Annotated[int, Field(ge=1, le=3000)]] | Annotated[int, Field(ge=1, le=3000)]
    xz_offset: IntProvider[Annotated[int, Field(ge=-16, le=16)]] | Annotated[int, Field(ge=-16, le=16)]
    y_offset: IntProvider[Annotated[int, Field(ge=-16, le=16)]] | Annotated[int, Field(ge=-16, le=16)]
