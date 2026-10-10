"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::FallenTreeConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/tree/FallenTreeConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.IntProvider import IntProvider
    from vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef import BlockStateProviderRef
    from vanilla_mcdoc.data.worldgen.feature.tree.TreeDecorator import TreeDecorator


class FallenTreeConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    trunk_provider: BlockStateProviderRef
    log_length: IntProvider[Annotated[int, Field(ge=0, le=16)]] | Annotated[int, Field(ge=0, le=16)]
    stump_decorators: list[TreeDecorator]
    log_decorators: list[TreeDecorator]
