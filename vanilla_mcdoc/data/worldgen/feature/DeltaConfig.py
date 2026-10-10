"""
Generated from symbols.json for ::java::data::worldgen::feature::DeltaConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/DeltaConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.IntProvider import IntProvider
    from vanilla_mcdoc.util.block_state.BlockState import BlockState


class DeltaConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    contents: BlockState
    rim: BlockState
    size: IntProvider[Annotated[int, Field(ge=0, le=16)]] | Annotated[int, Field(ge=0, le=16)]
    rim_size: IntProvider[Annotated[int, Field(ge=0, le=16)]] | Annotated[int, Field(ge=0, le=16)]
