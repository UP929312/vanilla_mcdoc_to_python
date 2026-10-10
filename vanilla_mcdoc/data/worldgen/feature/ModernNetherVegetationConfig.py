"""
Generated from symbols.json for ::java::data::worldgen::feature::ModernNetherVegetationConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/ModernNetherVegetationConfig.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class ModernNetherVegetationConfig(GeneratedModel):
    spread_width: Annotated[int, Field(ge=1)]
    spread_height: Annotated[int, Field(ge=1)]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::ModernNetherVegetationConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "spread_width",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1
                    }
                }
            },
            {
                "kind": "pair",
                "key": "spread_height",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1
                    }
                }
            }
        ]
    }
}
