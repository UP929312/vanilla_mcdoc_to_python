"""
Generated from symbols.json for ::java::data::worldgen::feature::placement::HeightmapModifier
Local link to file: vanilla_mcdoc/data/worldgen/feature/placement/HeightmapModifier.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.HeightmapType import HeightmapType


class HeightmapModifier(GeneratedModel):
    heightmap: HeightmapType


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::placement::HeightmapModifier": {
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
