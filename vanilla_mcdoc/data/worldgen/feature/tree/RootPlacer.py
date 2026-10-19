"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::RootPlacer
Local link to file: vanilla_mcdoc/data/worldgen/feature/tree/RootPlacer.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, Literal

from pydantic import Discriminator, Tag

from vanilla_mcdoc.base import tag_of
from vanilla_mcdoc.data.worldgen.feature.tree.MangroveRootPlacer import MangroveRootPlacer

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.IntProvider import IntProvider
    from vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef import BlockStateProviderRef
    from vanilla_mcdoc.data.worldgen.feature.tree.AboveRootPlacement import AboveRootPlacement


class RootPlacerMangroveRootPlacer(MangroveRootPlacer):
    type: Literal['minecraft:mangrove_root_placer', 'mangrove_root_placer'] = 'minecraft:mangrove_root_placer'
    root_provider: BlockStateProviderRef
    trunk_offset_y: IntProvider[int] | int
    above_root_placement: AboveRootPlacement | None = None


type RootPlacer = Annotated[
    Annotated[RootPlacerMangroveRootPlacer, Tag('minecraft:mangrove_root_placer')],
    Discriminator(tag_of('type')),
]
