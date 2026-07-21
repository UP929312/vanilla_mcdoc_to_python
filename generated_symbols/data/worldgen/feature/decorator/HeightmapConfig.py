# Generated from symbols.json for ::java::data::worldgen::feature::decorator::HeightmapConfig
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.HeightmapType import HeightmapType


@dataclass(kw_only=True)
class HeightmapConfig:
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

