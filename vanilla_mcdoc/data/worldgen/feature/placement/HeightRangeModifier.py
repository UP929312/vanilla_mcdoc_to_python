"""
Generated from symbols.json for ::java::data::worldgen::feature::placement::HeightRangeModifier
Local link to file: vanilla_mcdoc/data/worldgen/feature/placement/HeightRangeModifier.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.HeightProvider import HeightProvider


class HeightRangeModifier(GeneratedModel):
    height: HeightProvider


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::placement::HeightRangeModifier": {
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
        ]
    }
}
