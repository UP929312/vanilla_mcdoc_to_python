"""
Generated from symbols.json for ::java::data::worldgen::feature::HugeMushroomConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/HugeMushroomConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.block_predicate.BlockPredicate import BlockPredicate
    from vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef import BlockStateProviderRef


class HugeMushroomConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    cap_provider: BlockStateProviderRef
    stem_provider: BlockStateProviderRef
    foliage_radius: int
    can_place_on: BlockPredicate
