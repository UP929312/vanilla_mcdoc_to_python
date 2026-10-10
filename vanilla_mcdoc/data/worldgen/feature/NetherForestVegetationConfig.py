"""
Generated from symbols.json for ::java::data::worldgen::feature::NetherForestVegetationConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/NetherForestVegetationConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef import BlockStateProviderRef


class NetherForestVegetationConfig(GeneratedModel):
    state_provider: BlockStateProviderRef
    spread_width: Annotated[int, Field(ge=1)]
    spread_height: Annotated[int, Field(ge=1)]
