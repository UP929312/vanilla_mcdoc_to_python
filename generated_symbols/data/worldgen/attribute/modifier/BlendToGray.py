"""
Generated from symbols.json for ::java::data::worldgen::attribute::modifier::BlendToGray
Local link to file: generated_symbols/data/worldgen/attribute/modifier/BlendToGray.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel


class BlendToGray(GeneratedModel):
    brightness: Annotated[float, Field(ge=0, le=1)]  # The gray color is `brightness * (0.3 * r + 0.59 * g + 0.11 * b)`.
    factor: Annotated[float, Field(ge=0, le=1)]  # The factor to mix with.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::attribute::modifier::BlendToGray": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The gray color is `brightness * (0.3 * r + 0.59 * g + 0.11 * b)`.",
                "key": "brightness",
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
                "desc": "The factor to mix with.",
                "key": "factor",
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

