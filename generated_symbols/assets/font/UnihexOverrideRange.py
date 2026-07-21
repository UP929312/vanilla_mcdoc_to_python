# Generated from symbols.json for ::java::assets::font::UnihexOverrideRange
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class UnihexOverrideRange:
    from_: str  # Minimum in codepoint range (inclusive).
    to: str  # Maximum in codepoint range (inclusive).
    left: Annotated[int, 'Range | `0`-`255` | both inclusive']  # Position of left-most column of the glyph.
    right: Annotated[int, 'Range | `0`-`255` | both inclusive']  # Position of right-most column of the glyph.


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

