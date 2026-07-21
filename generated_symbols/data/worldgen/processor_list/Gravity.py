# Generated from symbols.json for ::java::data::worldgen::processor_list::Gravity
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.HeightmapType import HeightmapType


@dataclass(kw_only=True)
class Gravity:
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

