"""
Generated from symbols.json for ::java::data::worldgen::processor_list::Gravity
Local link to file: vanilla_mcdoc/data/worldgen/processor_list/Gravity.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.HeightmapType import HeightmapType


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
