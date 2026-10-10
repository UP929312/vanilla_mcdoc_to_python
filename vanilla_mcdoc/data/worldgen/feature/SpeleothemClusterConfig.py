"""
Generated from symbols.json for ::java::data::worldgen::feature::SpeleothemClusterConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/SpeleothemClusterConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.FloatProvider import FloatProvider
    from vanilla_mcdoc.data.worldgen.IntProvider import IntProvider
    from vanilla_mcdoc.data.worldgen.feature.SpeleothemBaseBlockTransformer import SpeleothemBaseBlockTransformer
    from vanilla_mcdoc.data.worldgen.feature.SpeleothemClusterPlacementMode import SpeleothemClusterPlacementMode
    from vanilla_mcdoc.registry.KnownBlockId import KnownBlockId
    from vanilla_mcdoc.util.block_state.BlockState import BlockState


class PlacementOptionsStruct(GeneratedModel):
    placement_mode: SpeleothemClusterPlacementMode
    base_block_transformer: SpeleothemBaseBlockTransformer
    allow_water_placement: bool


class SpeleothemClusterConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    base_block: BlockState
    pointed_block: BlockState
    replaceable_blocks: list[Annotated[str, IdSpec(registry='block')] | KnownBlockId] | Annotated[str, IdSpec(registry='block', tags='allowed')] | KnownBlockId
    floor_to_ceiling_search_range: Annotated[int, Field(ge=1, le=512)]
    height: IntProvider[Annotated[int, Field(ge=0, le=128)]] | Annotated[int, Field(ge=0, le=128)]
    radius: IntProvider[Annotated[int, Field(ge=0, le=128)]] | Annotated[int, Field(ge=0, le=128)]
    max_stalagmite_stalactite_height_diff: Annotated[int, Field(ge=0, le=64)]  # Max height difference between the stalagmite and stalactite.
    height_deviation: Annotated[int, Field(ge=1, le=64)]
    speleothem_block_layer_thickness: IntProvider[Annotated[int, Field(ge=0, le=128)]] | Annotated[int, Field(ge=0, le=128)]
    density: FloatProvider[Annotated[float, Field(ge=0, le=2)]] | Annotated[float, Field(ge=0, le=2)]
    wetness: FloatProvider[Annotated[float, Field(ge=0, le=2)]] | Annotated[float, Field(ge=0, le=2)]
    chance_of_speleothem_at_max_distance_from_center: Annotated[float, Field(ge=0, le=1)]
    max_distance_from_edge_affecting_chance_of_speleothem: Annotated[int, Field(ge=1, le=64)]
    max_distance_from_center_affecting_height_bias: Annotated[int, Field(ge=1, le=64)]
    placement_options: PlacementOptionsStruct | None = None
