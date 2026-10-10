"""
Generated from symbols.json for ::java::data::worldgen::feature::ColumnsConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/ColumnsConfig.py
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


class ColumnsConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    block: BlockStateProviderRef
    can_replace: BlockPredicate
    continue_through: BlockPredicate
    cannot_place_on: Annotated[str, IdSpec(registry='block', tags='allowed')] | KnownBlockId | list[Annotated[str, IdSpec(registry='block')] | KnownBlockId]
    column_reach: IntProvider[Annotated[int, Field(ge=0, le=3)]] | Annotated[int, Field(ge=0, le=3)]
    column_count: IntProvider[Annotated[int, Field(ge=1, le=150)]] | Annotated[int, Field(ge=1, le=150)]
    height: IntProvider[Annotated[int, Field(ge=1, le=10)]] | Annotated[int, Field(ge=1, le=10)]
    cluster_reach: IntProvider[Annotated[int, Field(ge=0, le=13)]] | Annotated[int, Field(ge=0, le=13)]  # The effective reach is limited by `height`.
