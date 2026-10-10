"""
Generated from symbols.json for ::java::data::worldgen::feature::decorator::WaterDepthThresholdConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/decorator/WaterDepthThresholdConfig.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class WaterDepthThresholdConfig(GeneratedModel):
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
