"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::AboveRootPlacement
Local link to file: vanilla_mcdoc/data/worldgen/feature/tree/AboveRootPlacement.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef import BlockStateProviderRef


class AboveRootPlacement(GeneratedModel):
    above_root_provider: BlockStateProviderRef
    above_root_placement_chance: Annotated[float, Field(ge=0, le=1)]
