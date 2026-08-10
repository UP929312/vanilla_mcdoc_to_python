"""
Generated from symbols.json for ::java::data::worldgen::structure::WildUpdateStructureConfig
Local link to file: generated_symbols/data/worldgen/structure/WildUpdateStructureConfig.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

from runtime_metadata import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.HeightProvider import HeightProvider
    from generated_symbols.data.worldgen.HeightmapType import HeightmapType
    from generated_symbols.data.worldgen.structure.JigsawDistanceLimits import JigsawDistanceLimits


@dataclass(kw_only=True)
class WildUpdateStructureConfig:
    start_height: HeightProvider
    max_distance_from_center: Annotated[int, 'Range | `1`-`128` | both inclusive'] | JigsawDistanceLimits[Annotated[int, 'Range | `1`-`128` | both inclusive']] | Annotated[int, 'Range | `1`-`128` | both inclusive'] | Annotated[int, 'Range | `1`-`116` | both inclusive'] | JigsawDistanceLimits[Annotated[int, 'Range | `1`-`116` | both inclusive']] | Annotated[int, 'Range | `1`-`116` | both inclusive']
    use_expansion_hack: bool
    start_jigsaw_name: Annotated[str, IdSpec()] | None = None
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

