"""
Generated from symbols.json for ::java::assets::texture_meta::NineSliceBorder
Local link to file: generated_symbols/assets/texture_meta/NineSliceBorder.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class NineSliceBorder:
    left: Annotated[int, 'Range | Min `0` and above | inclusive']
    top: Annotated[int, 'Range | Min `0` and above | inclusive']
    right: Annotated[int, 'Range | Min `0` and above | inclusive']
    bottom: Annotated[int, 'Range | Min `0` and above | inclusive']


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

