"""
Generated from symbols.json for ::java::data::worldgen::feature::decorator::RangeConfig
Local link to file: generated_symbols/data/worldgen/feature/decorator/RangeConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.HeightProvider import HeightProvider


class RangeConfig(GeneratedModel):
    height: HeightProvider


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::decorator::RangeConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "height",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::HeightProvider"
                }
            }
        ],
        "attributes": [
            {
                "name": "since",
                "value": {
                    "kind": "literal",
                    "value": {
                        "kind": "string",
                        "value": "1.17"
                    }
                }
            }
        ]
    }
}

