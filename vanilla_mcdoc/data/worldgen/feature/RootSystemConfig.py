"""
Generated from symbols.json for ::java::data::worldgen::feature::RootSystemConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/RootSystemConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.FeatureRef import FeatureRef
    from vanilla_mcdoc.data.worldgen.feature.block_predicate.BlockPredicate import BlockPredicate
    from vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef import BlockStateProviderRef
    from vanilla_mcdoc.registry.KnownBlockId import KnownBlockId


class RootSystemConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    required_vertical_space_for_tree: Annotated[int, Field(ge=1, le=64)]
    level_test_distance: Annotated[int, Field(ge=0, le=16)]
    max_level_deviation: Annotated[int, Field(ge=0, le=64)]
    root_radius: Annotated[int, Field(ge=1, le=64)]
    root_placement_attempts: Annotated[int, Field(ge=1, le=256)]
    root_column_max_height: Annotated[int, Field(ge=1, le=4096)]
    hanging_root_radius: Annotated[int, Field(ge=1, le=64)]
    hanging_roots_vertical_span: Annotated[int, Field(ge=1, le=16)]
    hanging_root_placement_attempts: Annotated[int, Field(ge=0, le=256)]
    allowed_vertical_water_for_tree: Annotated[int, Field(ge=1, le=64)]
    root_replaceable: Annotated[str, IdSpec(registry='block', tags='allowed')] | KnownBlockId | list[Annotated[str, IdSpec(registry='block')] | KnownBlockId]
    root_state_provider: BlockStateProviderRef
    hanging_root_state_provider: BlockStateProviderRef
    allowed_tree_position: BlockPredicate
    feature: FeatureRef
