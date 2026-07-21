# Generated from symbols.json for ::java::data::worldgen::feature::placement::HeightmapModifier
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.HeightmapType import HeightmapType


@dataclass(kw_only=True)
class HeightmapModifier:
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

