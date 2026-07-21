# Generated from symbols.json for ::java::data::worldgen::attribute::modifier::BlendToGray
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class BlendToGray:
    brightness: Annotated[float, 'Range | `0`-`1` | both inclusive']  # The gray color is `brightness * (0.3 * r + 0.59 * g + 0.11 * b)`.
    factor: Annotated[float, 'Range | `0`-`1` | both inclusive']  # The factor to mix with.


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

