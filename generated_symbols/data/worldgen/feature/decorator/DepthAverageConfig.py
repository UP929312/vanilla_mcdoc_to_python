# Generated from symbols.json for ::java::data::worldgen::feature::decorator::DepthAverageConfig
from dataclasses import dataclass


@dataclass(kw_only=True)
class DepthAverageConfig:
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

