"""
Generated from symbols.json for ::java::data::worldgen::feature::decorator::HeightmapConfig
Local link to file: generated_symbols/data/worldgen/feature/decorator/HeightmapConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.HeightmapType import HeightmapType


class HeightmapConfig(GeneratedModel):
    heightmap: HeightmapType


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::decorator::HeightmapConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "heightmap",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::HeightmapType"
                }
            }
        ]
    }
}

