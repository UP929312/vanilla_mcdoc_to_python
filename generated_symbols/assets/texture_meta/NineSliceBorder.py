"""
Generated from symbols.json for ::java::assets::texture_meta::NineSliceBorder
Local link to file: generated_symbols/assets/texture_meta/NineSliceBorder.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from generated_symbols.base import GeneratedModel
from pydantic import Field


class NineSliceBorder(GeneratedModel):
    left: Annotated[int, Field(ge=0)]
    top: Annotated[int, Field(ge=0)]
    right: Annotated[int, Field(ge=0)]
    bottom: Annotated[int, Field(ge=0)]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::texture_meta::NineSliceBorder": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "left",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                }
            },
            {
                "kind": "pair",
                "key": "top",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                }
            },
            {
                "kind": "pair",
                "key": "right",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                }
            },
            {
                "kind": "pair",
                "key": "bottom",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                }
            }
        ]
    }
}

