# Generated from symbols.json for ::java::data::worldgen::structure::WildUpdateStructureConfig
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.HeightProvider import HeightProvider
    from generated_symbols.data.worldgen.HeightmapType import HeightmapType


@dataclass(kw_only=True)
class WildUpdateStructureConfig:
    start_height: HeightProvider
    max_distance_from_center: Any
    use_expansion_hack: bool
    start_jigsaw_name: str | None = None
    project_start_to_heightmap: HeightmapType | None = None


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

