"""
Generated from symbols.json for ::java::data::worldgen::feature::decorator::DepthAverageConfig
Local link to file: generated_symbols/data/worldgen/feature/decorator/DepthAverageConfig.py
"""
# ~~~ CODE ~~~
from generated_symbols.base import GeneratedModel


class DepthAverageConfig(GeneratedModel):
    baseline: int
    spread: int


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::decorator::DepthAverageConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "baseline",
                "type": {
                    "kind": "int"
                }
            },
            {
                "kind": "pair",
                "key": "spread",
                "type": {
                    "kind": "int"
                }
            }
        ]
    }
}
