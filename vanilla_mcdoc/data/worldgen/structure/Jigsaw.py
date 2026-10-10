"""
Generated from symbols.json for ::java::data::worldgen::structure::Jigsaw
Local link to file: vanilla_mcdoc/data/worldgen/structure/Jigsaw.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.HeightProvider import HeightProvider
    from vanilla_mcdoc.data.worldgen.HeightmapType import HeightmapType
    from vanilla_mcdoc.data.worldgen.structure.JigsawDistanceLimits import JigsawDistanceLimits
    from vanilla_mcdoc.data.worldgen.structure.LiquidSettings import LiquidSettings
    from vanilla_mcdoc.data.worldgen.structure.PoolAlias import PoolAlias


class DimensionPaddingStruct(GeneratedModel):
    bottom: Annotated[int, Field(ge=0)] | None = None
    top: Annotated[int, Field(ge=0)] | None = None


class Jigsaw(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/structure'

    start_pool: Annotated[str, IdSpec(registry='worldgen/template_pool')]
    size: Annotated[int, Field(ge=1, le=20)]
    start_height: HeightProvider
    start_jigsaw_name: Annotated[str, IdSpec()] | None = None
    project_start_to_heightmap: HeightmapType | None = None
    max_distance_from_center: Annotated[int, Field(ge=1, le=128)] | JigsawDistanceLimits[Annotated[int, Field(ge=1, le=128)]] | Annotated[int, Field(ge=1, le=128)] | Annotated[int, Field(ge=1, le=116)] | JigsawDistanceLimits[Annotated[int, Field(ge=1, le=116)]] | Annotated[int, Field(ge=1, le=116)]
    use_expansion_hack: bool
    pool_aliases: list[PoolAlias] | None = None
    dimension_padding: Annotated[int, Field(ge=0)] | DimensionPaddingStruct | None = None
    liquid_settings: LiquidSettings | None = None
