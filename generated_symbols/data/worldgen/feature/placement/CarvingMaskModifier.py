"""
Generated from symbols.json for ::java::data::worldgen::feature::placement::CarvingMaskModifier
Local link to file: generated_symbols/data/worldgen/feature/placement/CarvingMaskModifier.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.CarveStep import CarveStep


@dataclass(kw_only=True)
class CarvingMaskModifier:
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

