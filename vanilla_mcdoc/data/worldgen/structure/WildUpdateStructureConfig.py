"""
Generated from symbols.json for ::java::data::worldgen::structure::WildUpdateStructureConfig
Local link to file: vanilla_mcdoc/data/worldgen/structure/WildUpdateStructureConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.HeightProvider import HeightProvider
    from vanilla_mcdoc.data.worldgen.HeightmapType import HeightmapType
    from vanilla_mcdoc.data.worldgen.structure.JigsawDistanceLimits import JigsawDistanceLimits


class WildUpdateStructureConfig(GeneratedModel):
    start_height: HeightProvider
    start_jigsaw_name: Annotated[str, IdSpec()] | None = None
    project_start_to_heightmap: HeightmapType | None = None
    max_distance_from_center: Annotated[int, Field(ge=1, le=128)] | JigsawDistanceLimits[Annotated[int, Field(ge=1, le=128)]] | Annotated[int, Field(ge=1, le=128)] | Annotated[int, Field(ge=1, le=116)] | JigsawDistanceLimits[Annotated[int, Field(ge=1, le=116)]] | Annotated[int, Field(ge=1, le=116)]
    use_expansion_hack: bool
