"""
Generated from symbols.json for ::java::data::worldgen::feature::placement::SurfaceRelativeThresholdFilter
Local link to file: generated_symbols/data/worldgen/feature/placement/SurfaceRelativeThresholdFilter.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.HeightmapType import HeightmapType


class SurfaceRelativeThresholdFilter(GeneratedModel):
    heightmap: HeightmapType
    min_inclusive: int | None = None
    max_inclusive: int | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::placement::SurfaceRelativeThresholdFilter": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "heightmap",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::HeightmapType"
                }
            },
            {
                "kind": "pair",
                "key": "min_inclusive",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "max_inclusive",
                "type": {
                    "kind": "int"
                },
                "optional": True
            }
        ]
    }
}
