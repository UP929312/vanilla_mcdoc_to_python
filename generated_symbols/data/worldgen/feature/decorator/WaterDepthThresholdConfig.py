"""
Generated from symbols.json for ::java::data::worldgen::feature::decorator::WaterDepthThresholdConfig
Local link to file: generated_symbols/data/worldgen/feature/decorator/WaterDepthThresholdConfig.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass


@dataclass(kw_only=True)
class WaterDepthThresholdConfig:
    max_water_depth: int


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::decorator::WaterDepthThresholdConfig": {
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

