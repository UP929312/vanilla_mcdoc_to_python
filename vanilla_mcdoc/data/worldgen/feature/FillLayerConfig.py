"""
Generated from symbols.json for ::java::data::worldgen::feature::FillLayerConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/FillLayerConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.block_state.BlockState import BlockState


class FillLayerConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    state: BlockState
    height: Annotated[int, Field(ge=0, le=255)]
