"""
Generated from symbols.json for ::java::data::worldgen::feature::EmeraldOreConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/EmeraldOreConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.block_state.BlockState import BlockState


class EmeraldOreConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    state: BlockState
    target: BlockState
