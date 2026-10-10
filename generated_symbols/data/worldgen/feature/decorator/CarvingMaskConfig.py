"""
Generated from symbols.json for ::java::data::worldgen::feature::decorator::CarvingMaskConfig
Local link to file: generated_symbols/data/worldgen/feature/decorator/CarvingMaskConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.CarveStep import CarveStep


class CarvingMaskConfig(GeneratedModel):
    step: CarveStep


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::decorator::CarvingMaskConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "step",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::CarveStep"
                }
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.17"
                            }
                        }
                    }
                ],
                "key": "probability",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1
                    }
                }
            }
        ]
    }
}
