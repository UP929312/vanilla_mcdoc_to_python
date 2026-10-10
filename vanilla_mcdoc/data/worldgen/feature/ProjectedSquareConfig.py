"""
Generated from symbols.json for ::java::data::worldgen::feature::ProjectedSquareConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/ProjectedSquareConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.IntProvider import IntProvider
    from vanilla_mcdoc.data.worldgen.feature.block_predicate.BlockPredicate import BlockPredicate
    from vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef import BlockStateProviderRef


class ProjectedSquareConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    block: BlockStateProviderRef
    project_through: BlockPredicate
    size: IntProvider[Annotated[int, Field(ge=1, le=16)]] | Annotated[int, Field(ge=1, le=16)]
    max_projection_height: Annotated[int, Field(ge=0)]
