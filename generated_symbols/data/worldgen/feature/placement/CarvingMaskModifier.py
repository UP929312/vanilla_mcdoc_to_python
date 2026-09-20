"""
Generated from symbols.json for ::java::data::worldgen::feature::placement::CarvingMaskModifier
Local link to file: generated_symbols/data/worldgen/feature/placement/CarvingMaskModifier.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.CarveStep import CarveStep


class CarvingMaskModifier(GeneratedModel):
    step: CarveStep


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::placement::CarvingMaskModifier": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "step",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::CarveStep"
                }
            }
        ]
    }
}

