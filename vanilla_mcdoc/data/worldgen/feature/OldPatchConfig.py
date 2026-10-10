"""
Generated from symbols.json for ::java::data::worldgen::feature::OldPatchConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/OldPatchConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.BlockPlacer import BlockPlacer
    from vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef import BlockStateProviderRef
    from vanilla_mcdoc.util.block_state.BlockState import BlockState


class OldPatchConfig(GeneratedModel):
    can_replace: bool | None = None
    project: bool | None = None
    need_water: bool | None = None
    xspread: Annotated[int, Field(ge=0)] | None = None
    yspread: Annotated[int, Field(ge=0)] | None = None
    zspread: Annotated[int, Field(ge=0)] | None = None
    state_provider: BlockStateProviderRef
    block_placer: BlockPlacer
    whitelist: list[BlockState]
    blacklist: list[BlockState]
