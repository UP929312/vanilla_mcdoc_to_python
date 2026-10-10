"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::AttachedToLogsTreeDecorator
Local link to file: vanilla_mcdoc/data/worldgen/feature/tree/AttachedToLogsTreeDecorator.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef import BlockStateProviderRef
    from vanilla_mcdoc.util.direction.Direction import Direction


class AttachedToLogsTreeDecorator(GeneratedModel):
    probability: Annotated[float, Field(ge=0, le=1)]
    block_provider: BlockStateProviderRef
    directions: Annotated[list[Direction], Field(min_length=1)]
