# Generated from symbols.json for ::java::assets::texture_meta::MipmapStrategy
from enum import Enum


class MipmapStrategy(Enum):
    AUTO = "auto"
    MEAN = "mean"
    CUTOUT = "cutout"
    STRICTCUTOUT = "strict_cutout"
    DARKCUTOUT = "dark_cutout"


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::texture_meta::MipmapStrategy": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "identifier": "Auto",
                "value": "auto"
            },
            {
                "identifier": "Mean",
                "value": "mean"
            },
            {
                "identifier": "Cutout",
                "value": "cutout"
            },
            {
                "identifier": "StrictCutout",
                "value": "strict_cutout"
            },
            {
                "identifier": "DarkCutout",
                "value": "dark_cutout"
            }
        ]
    }
}

