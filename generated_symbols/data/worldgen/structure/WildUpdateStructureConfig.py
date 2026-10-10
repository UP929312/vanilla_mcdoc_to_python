"""
Generated from symbols.json for ::java::data::worldgen::structure::WildUpdateStructureConfig
Local link to file: generated_symbols/data/worldgen/structure/WildUpdateStructureConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel
from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.HeightProvider import HeightProvider
    from generated_symbols.data.worldgen.HeightmapType import HeightmapType
    from generated_symbols.data.worldgen.structure.JigsawDistanceLimits import JigsawDistanceLimits


class WildUpdateStructureConfig(GeneratedModel):
    start_height: HeightProvider
    start_jigsaw_name: Annotated[str, IdSpec()] | None = None
    project_start_to_heightmap: HeightmapType | None = None
    max_distance_from_center: Annotated[int, Field(ge=1, le=128)] | JigsawDistanceLimits[Annotated[int, Field(ge=1, le=128)]] | Annotated[int, Field(ge=1, le=128)] | Annotated[int, Field(ge=1, le=116)] | JigsawDistanceLimits[Annotated[int, Field(ge=1, le=116)]] | Annotated[int, Field(ge=1, le=116)]
    use_expansion_hack: bool


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::structure::WildUpdateStructureConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "start_height",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::HeightProvider"
                }
            },
            {
                "kind": "pair",
                "key": "start_jigsaw_name",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id"
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "project_start_to_heightmap",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::HeightmapType"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "max_distance_from_center",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "terrain_adaptation"
                            ]
                        }
                    ],
                    "registry": "minecraft:jigsaw_max_distance_from_center"
                }
            },
            {
                "kind": "pair",
                "key": "use_expansion_hack",
                "type": {
                    "kind": "boolean"
                }
            }
        ]
    }
}

