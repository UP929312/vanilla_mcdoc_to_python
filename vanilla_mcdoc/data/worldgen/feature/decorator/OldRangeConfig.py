"""
Generated from symbols.json for ::java::data::worldgen::feature::decorator::OldRangeConfig
Local link to file: generated_symbols/data/worldgen/feature/decorator/OldRangeConfig.py
"""
# ~~~ CODE ~~~
from generated_symbols.base import GeneratedModel


class OldRangeConfig(GeneratedModel):
    maximum: int
    bottom_offset: int
    top_offset: int


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::decorator::OldRangeConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "maximum",
                "type": {
                    "kind": "int"
                }
            },
            {
                "kind": "pair",
                "key": "bottom_offset",
                "type": {
                    "kind": "int"
                }
            },
            {
                "kind": "pair",
                "key": "top_offset",
                "type": {
                    "kind": "int"
                }
            }
        ]
    }
}
