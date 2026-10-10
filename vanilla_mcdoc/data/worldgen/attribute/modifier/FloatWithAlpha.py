"""
Generated from symbols.json for ::java::data::worldgen::attribute::modifier::FloatWithAlpha
Local link to file: generated_symbols/data/worldgen/attribute/modifier/FloatWithAlpha.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel


class FloatWithAlpha(GeneratedModel):
    value: float
    alpha: Annotated[float, Field(ge=0, le=1)] | None = None  # Defaults to 1.0


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::attribute::modifier::FloatWithAlpha": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "value",
                "type": {
                    "kind": "float"
                }
            },
            {
                "kind": "pair",
                "desc": "Defaults to 1.0",
                "key": "alpha",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1
                    }
                },
                "optional": True
            }
        ]
    }
}
