"""
Generated from symbols.json for ::java::data::worldgen::feature::block_state_provider::BlockStateProviderRef
Local link to file: vanilla_mcdoc/data/worldgen/feature/block_state_provider/BlockStateProviderRef.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProvider import BlockStateProvider


type BlockStateProviderRef = BlockStateProvider | Annotated[str, IdSpec(registry='worldgen/block_state_provider')]
