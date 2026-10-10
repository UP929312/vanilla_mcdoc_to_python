"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::HeightFoliagePlacer
Local link to file: generated_symbols/data/worldgen/feature/tree/HeightFoliagePlacer.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel


class HeightFoliagePlacer(GeneratedModel):
    height: Annotated[int, Field(ge=0, le=16)]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::tree::HeightFoliagePlacer": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "height",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 16
                    }
                }
            }
        ]
    }
}

