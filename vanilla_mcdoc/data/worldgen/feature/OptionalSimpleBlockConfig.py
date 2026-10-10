"""
Generated from symbols.json for ::java::data::worldgen::feature::OptionalSimpleBlockConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/OptionalSimpleBlockConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.block_state.BlockState import BlockState


class OptionalSimpleBlockConfig(GeneratedModel):
    place_on: list[BlockState] | None = None
    place_in: list[BlockState] | None = None
    place_under: list[BlockState] | None = None
