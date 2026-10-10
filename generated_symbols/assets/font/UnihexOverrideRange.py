"""
Generated from symbols.json for ::java::assets::font::UnihexOverrideRange
Local link to file: generated_symbols/assets/font/UnihexOverrideRange.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel


class UnihexOverrideRange(GeneratedModel):
    from_: str = Field(alias='from')  # Minimum in codepoint range (inclusive).
    to: str  # Maximum in codepoint range (inclusive).
    left: Annotated[int, Field(ge=0, le=255)]  # Position of left-most column of the glyph.
    right: Annotated[int, Field(ge=0, le=255)]  # Position of right-most column of the glyph.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::font::UnihexOverrideRange": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Minimum in codepoint range (inclusive).",
                "key": "from",
                "type": {
                    "kind": "string"
                }
            },
            {
                "kind": "pair",
                "desc": "Maximum in codepoint range (inclusive).",
                "key": "to",
                "type": {
                    "kind": "string"
                }
            },
            {
                "kind": "pair",
                "desc": "Position of left-most column of the glyph.",
                "key": "left",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 255
                    }
                }
            },
            {
                "kind": "pair",
                "desc": "Position of right-most column of the glyph.",
                "key": "right",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 255
                    }
                }
            }
        ]
    }
}

