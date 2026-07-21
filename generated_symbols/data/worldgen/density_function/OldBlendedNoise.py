# Generated from symbols.json for ::java::data::worldgen::density_function::OldBlendedNoise
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class OldBlendedNoise:
    xz_scale: float
    y_scale: float
    xz_factor: float
    y_factor: float
    smear_scale_multiplier: Annotated[float, 'Range | `1`-`8` | both inclusive']


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::density_function::OldBlendedNoise": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "xz_scale",
                "type": {
                    "kind": "float"
                }
            },
            {
                "kind": "pair",
                "key": "y_scale",
                "type": {
                    "kind": "float"
                }
            },
            {
                "kind": "pair",
                "key": "xz_factor",
                "type": {
                    "kind": "float"
                }
            },
            {
                "kind": "pair",
                "key": "y_factor",
                "type": {
                    "kind": "float"
                }
            },
            {
                "kind": "pair",
                "key": "smear_scale_multiplier",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 1,
                        "max": 8
                    }
                }
            }
        ]
    }
}

