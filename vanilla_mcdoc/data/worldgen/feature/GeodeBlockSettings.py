"""
Generated from symbols.json for ::java::data::worldgen::feature::GeodeBlockSettings
Local link to file: vanilla_mcdoc/data/worldgen/feature/GeodeBlockSettings.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef import BlockStateProviderRef
    from vanilla_mcdoc.registry.KnownBlockId import KnownBlockId
    from vanilla_mcdoc.util.block_state.BlockState import BlockState


class GeodeBlockSettings(GeneratedModel):
    filling_provider: BlockStateProviderRef
    inner_layer_provider: BlockStateProviderRef
    alternate_inner_layer_provider: BlockStateProviderRef
    middle_layer_provider: BlockStateProviderRef
    outer_layer_provider: BlockStateProviderRef
    inner_placements: Annotated[list[BlockState], Field(min_length=1)]
    cannot_replace: Annotated[str, IdSpec(registry='block', tags='allowed')] | KnownBlockId | list[Annotated[str, IdSpec(registry='block')] | KnownBlockId]  # Blocks that will not be replaced by the geode.
    invalid_blocks: Annotated[str, IdSpec(registry='block', tags='allowed')] | KnownBlockId | list[Annotated[str, IdSpec(registry='block')] | KnownBlockId]  # When encountering an invalid block, feature placement is cancelled.
