"""
Generated from symbols.json for ::java::data::worldgen::feature::LargeSpeleothemConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/LargeSpeleothemConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.FloatProvider import FloatProvider
    from vanilla_mcdoc.data.worldgen.IntProvider import IntProvider
    from vanilla_mcdoc.registry.KnownBlockId import KnownBlockId
    from vanilla_mcdoc.util.block_state.BlockState import BlockState


class LargeSpeleothemConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    base_block: BlockState
    replaceable_blocks: list[Annotated[str, IdSpec(registry='block')] | KnownBlockId] | Annotated[str, IdSpec(registry='block', tags='allowed')] | KnownBlockId
    floor_to_ceiling_search_range: Annotated[int, Field(ge=1, le=512)] | None = None
    column_radius: IntProvider[Annotated[int, Field(ge=0, le=16)]] | Annotated[int, Field(ge=0, le=16)]
    height_scale: FloatProvider[Annotated[float, Field(ge=0, le=20)]] | Annotated[float, Field(ge=0, le=20)]
    max_column_radius_to_cave_height_ratio: Annotated[float, Field(ge=0, le=1)]
    stalactite_bluntness: FloatProvider[Annotated[float, Field(ge=0.1, le=10)]] | Annotated[float, Field(ge=0.1, le=10)]
    stalagmite_bluntness: FloatProvider[Annotated[float, Field(ge=0.1, le=10)]] | Annotated[float, Field(ge=0.1, le=10)]
    wind_speed: FloatProvider[Annotated[float, Field(ge=0, le=2)]] | Annotated[float, Field(ge=0, le=2)]
    min_radius_for_wind: Annotated[int, Field(ge=0, le=100)]
    min_bluntness_for_wind: Annotated[float, Field(ge=0, le=1)]
