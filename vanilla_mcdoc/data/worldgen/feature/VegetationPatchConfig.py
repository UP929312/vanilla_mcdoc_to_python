"""
Generated from symbols.json for ::java::data::worldgen::feature::VegetationPatchConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/VegetationPatchConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.CaveSurface import CaveSurface
    from vanilla_mcdoc.data.worldgen.IntProvider import IntProvider
    from vanilla_mcdoc.data.worldgen.feature.FeatureRef import FeatureRef
    from vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef import BlockStateProviderRef
    from vanilla_mcdoc.registry.KnownBlockId import KnownBlockId


class VegetationPatchConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    surface: CaveSurface
    depth: IntProvider[Annotated[int, Field(ge=1, le=128)]] | Annotated[int, Field(ge=1, le=128)]
    vertical_range: Annotated[int, Field(ge=1, le=256)]
    extra_bottom_block_chance: Annotated[float, Field(ge=0, le=1)]
    extra_edge_column_chance: Annotated[float, Field(ge=0, le=1)]
    vegetation_chance: Annotated[float, Field(ge=0, le=1)]
    xz_radius: IntProvider[int] | int
    replaceable: Annotated[str, IdSpec(registry='block', tags='allowed')] | KnownBlockId | list[Annotated[str, IdSpec(registry='block')] | KnownBlockId]
    ground_state: BlockStateProviderRef
    vegetation_feature: FeatureRef
