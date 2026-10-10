"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::PaleMossTreeDecorator
Local link to file: generated_symbols/data/worldgen/feature/tree/PaleMossTreeDecorator.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel


class PaleMossTreeDecorator(GeneratedModel):
    leaves_probability: Annotated[float, Field(ge=0, le=1)]
    trunk_probability: Annotated[float, Field(ge=0, le=1)]
    ground_probability: Annotated[float, Field(ge=0, le=1)]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::tree::PaleMossTreeDecorator": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "leaves_probability",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1
                    }
                }
            },
            {
                "kind": "pair",
                "key": "trunk_probability",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1
                    }
                }
            },
            {
                "kind": "pair",
                "key": "ground_probability",
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

