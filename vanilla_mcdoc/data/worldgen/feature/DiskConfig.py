"""
Generated from symbols.json for ::java::data::worldgen::feature::DiskConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/DiskConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.IntProvider import IntProvider
    from vanilla_mcdoc.data.worldgen.feature.block_predicate.BlockPredicate import BlockPredicate
    from vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef import BlockStateProviderRef


class DiskConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    state_provider: BlockStateProviderRef
    radius: IntProvider[Annotated[int, Field(ge=0, le=8)]] | Annotated[int, Field(ge=0, le=8)]
    half_height: Annotated[int, Field(ge=0, le=4)]
    target: BlockPredicate
