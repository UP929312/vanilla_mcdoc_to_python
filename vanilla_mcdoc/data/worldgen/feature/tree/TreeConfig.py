"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::TreeConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/tree/TreeConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef import BlockStateProviderRef
    from vanilla_mcdoc.data.worldgen.feature.tree.FeatureSize import FeatureSize
    from vanilla_mcdoc.data.worldgen.feature.tree.FoliagePlacer import FoliagePlacer
    from vanilla_mcdoc.data.worldgen.feature.tree.RootPlacer import RootPlacer
    from vanilla_mcdoc.data.worldgen.feature.tree.TreeDecorator import TreeDecorator
    from vanilla_mcdoc.data.worldgen.feature.tree.TrunkPlacer import TrunkPlacer


class TreeConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    ignore_vines: bool | None = None
    minimum_size: FeatureSize
    below_trunk_provider: BlockStateProviderRef
    trunk_provider: BlockStateProviderRef
    foliage_provider: BlockStateProviderRef
    root_placer: RootPlacer | None = None
    trunk_placer: TrunkPlacer
    foliage_placer: FoliagePlacer
    decorators: list[TreeDecorator]
