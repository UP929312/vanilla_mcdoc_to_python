"""
Generated from symbols.json for ::java::assets::item_definition::GrassTint
Local link to file: generated_symbols/assets/item_definition/GrassTint.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel


class GrassTint(GeneratedModel):
    temperature: Annotated[float, Field(ge=0, le=1)]
    downfall: Annotated[float, Field(ge=0, le=1)]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::GrassTint": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "temperature",
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
                "key": "downfall",
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

