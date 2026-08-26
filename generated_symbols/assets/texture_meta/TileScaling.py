"""
Generated from symbols.json for ::java::assets::texture_meta::TileScaling
Local link to file: generated_symbols/assets/texture_meta/TileScaling.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class TileScaling:
    width: Annotated[int, 'Range | `1` and above | inclusive']
    height: Annotated[int, 'Range | `1` and above | inclusive']


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::texture_meta::TileScaling": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "width",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1
                    }
                }
            },
            {
                "kind": "pair",
                "key": "height",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1
                    }
                }
            }
        ]
    }
}

