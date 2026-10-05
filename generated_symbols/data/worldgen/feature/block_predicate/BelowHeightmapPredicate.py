"""
Generated from symbols.json for ::java::data::worldgen::feature::block_predicate::BelowHeightmapPredicate
Local link to file: generated_symbols/data/worldgen/feature/block_predicate/BelowHeightmapPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.HeightmapType import HeightmapType


class BelowHeightmapPredicate(GeneratedModel):
    heightmap: HeightmapType


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::block_predicate::BelowHeightmapPredicate": {
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

