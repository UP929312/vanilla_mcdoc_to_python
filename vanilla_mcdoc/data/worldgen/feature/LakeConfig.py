"""
Generated from symbols.json for ::java::data::worldgen::feature::LakeConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/LakeConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.block_predicate.BlockPredicate import BlockPredicate
    from vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef import BlockStateProviderRef


class LakeConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    fluid: BlockStateProviderRef
    barrier: BlockStateProviderRef
    can_place_feature: BlockPredicate
    can_replace_with_air_or_fluid: BlockPredicate
    can_replace_with_barrier: BlockPredicate
