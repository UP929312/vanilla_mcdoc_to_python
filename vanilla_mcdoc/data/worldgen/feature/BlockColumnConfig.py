"""
Generated from symbols.json for ::java::data::worldgen::feature::BlockColumnConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/BlockColumnConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.BlockColumnLayer import BlockColumnLayer
    from vanilla_mcdoc.data.worldgen.feature.block_predicate.BlockPredicate import BlockPredicate
    from vanilla_mcdoc.util.direction.Direction import Direction


class BlockColumnConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    direction: Direction
    allowed_placement: BlockPredicate
    prioritize_tip: bool
    layers: list[BlockColumnLayer]
