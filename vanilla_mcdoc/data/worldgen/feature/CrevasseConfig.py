"""
Generated from symbols.json for ::java::data::worldgen::feature::CrevasseConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/CrevasseConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.IntProvider import IntProvider
    from vanilla_mcdoc.data.worldgen.feature.block_predicate.BlockPredicate import BlockPredicate
    from vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef import BlockStateProviderRef


class CrevasseConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    max_width: Annotated[int, Field(ge=2, le=8)]
    max_length: Annotated[int, Field(ge=4, le=16)]
    min_footprint: Annotated[int, Field(ge=1, le=32)]
    cursor_surface_search_range: Annotated[int, Field(ge=1)]
    column_surface_search_range: Annotated[int, Field(ge=1)]
    twistiness: Annotated[float, Field(ge=0, le=16)]
    tapering: Annotated[float, Field(ge=0, le=1)]
    turn_factor: Annotated[float, Field(ge=0, le=1)]
    carve_depth: IntProvider[Annotated[int, Field(ge=1)]] | Annotated[int, Field(ge=1)]
    fill_depth: IntProvider[Annotated[int, Field(ge=1)]] | Annotated[int, Field(ge=1)]
    surface_block: BlockStateProviderRef
    fill_block: BlockStateProviderRef
    carvable_blocks: BlockPredicate
    acceptable_barrier: BlockPredicate
