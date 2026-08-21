"""
Generated from symbols.json for ::java::data::worldgen::density_function::TilingMode
Local link to file: generated_symbols/data/worldgen/density_function/TilingMode.py
"""
# ~~~ CODE ~~~
from enum import StrEnum


class TilingMode(StrEnum):
    CLAMPTOEDGE = "clamp_to_edge"
    REPEAT = "repeat"
    MIRROREDREPEAT = "mirrored_repeat"


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::density_function::TilingMode": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "identifier": "ClampToEdge",
                "value": "clamp_to_edge"
            },
            {
                "identifier": "Repeat",
                "value": "repeat"
            },
            {
                "identifier": "MirroredRepeat",
                "value": "mirrored_repeat"
            }
        ]
    }
}

