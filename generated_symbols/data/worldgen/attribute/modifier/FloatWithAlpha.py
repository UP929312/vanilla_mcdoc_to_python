"""
Generated from symbols.json for ::java::data::worldgen::attribute::modifier::FloatWithAlpha
Local link to file: generated_symbols/data/worldgen/attribute/modifier/FloatWithAlpha.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class FloatWithAlpha:
    value: float
    alpha: Annotated[float, 'Range | `0`-`1` | both inclusive'] | None = None  # Defaults to 1.0


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

