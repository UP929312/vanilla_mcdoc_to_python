"""
Generated from symbols.json for ::java::data::worldgen::feature::block_state_provider::RotatedStateProvider
Local link to file: vanilla_mcdoc/data/worldgen/feature/block_state_provider/RotatedStateProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef import BlockStateProviderRef
    from vanilla_mcdoc.util.direction.Direction import Direction


class RotatedStateProvider(GeneratedModel):
    state: BlockStateProviderRef
    direction: Direction | None = None
