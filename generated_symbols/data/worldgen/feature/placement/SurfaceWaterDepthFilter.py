"""
Generated from symbols.json for ::java::data::worldgen::feature::placement::SurfaceWaterDepthFilter
Local link to file: generated_symbols/data/worldgen/feature/placement/SurfaceWaterDepthFilter.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass


@dataclass(kw_only=True)
class SurfaceWaterDepthFilter:
    max_water_depth: int


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::placement::SurfaceWaterDepthFilter": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "max_water_depth",
                "type": {
                    "kind": "int"
                }
            }
        ]
    }
}

