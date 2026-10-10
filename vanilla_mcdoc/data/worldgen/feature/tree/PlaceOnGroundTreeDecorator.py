"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::PlaceOnGroundTreeDecorator
Local link to file: vanilla_mcdoc/data/worldgen/feature/tree/PlaceOnGroundTreeDecorator.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef import BlockStateProviderRef


class PlaceOnGroundTreeDecorator(GeneratedModel):
    tries: Annotated[int, Field(ge=1)] | None = None  # Defaults to `128`.
    radius: Annotated[int, Field(ge=0)] | None = None  # Defaults to `2`.
    height: Annotated[int, Field(ge=0)] | None = None  # Defaults to `1`.
    block_state_provider: BlockStateProviderRef  # The block to place on the ground.
