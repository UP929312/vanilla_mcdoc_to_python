"""
Generated from symbols.json for ::java::data::worldgen::feature::BlockPileConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/BlockPileConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef import BlockStateProviderRef


class BlockPileConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    state_provider: BlockStateProviderRef
