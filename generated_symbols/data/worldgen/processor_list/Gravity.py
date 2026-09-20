"""
Generated from symbols.json for ::java::data::worldgen::processor_list::Gravity
Local link to file: generated_symbols/data/worldgen/processor_list/Gravity.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.HeightmapType import HeightmapType


class Gravity(GeneratedModel):
    heightmap: HeightmapType
    offset: int


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::processor_list::Gravity": {
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
                "key": "offset",
                "type": {
                    "kind": "int"
                }
            }
        ]
    }
}

