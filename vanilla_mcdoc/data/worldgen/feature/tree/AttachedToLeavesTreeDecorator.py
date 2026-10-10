"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::AttachedToLeavesTreeDecorator
Local link to file: vanilla_mcdoc/data/worldgen/feature/tree/AttachedToLeavesTreeDecorator.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef import BlockStateProviderRef
    from vanilla_mcdoc.util.direction.Direction import Direction


class AttachedToLeavesTreeDecorator(GeneratedModel):
    probability: Annotated[float, Field(ge=0, le=1)]
    exclusion_radius_xz: Annotated[int, Field(ge=0, le=16)]
    exclusion_radius_y: Annotated[int, Field(ge=0, le=16)]
    required_empty_blocks: Annotated[int, Field(ge=1, le=16)]
    block_provider: BlockStateProviderRef
    directions: Annotated[list[Direction], Field(min_length=1)]
