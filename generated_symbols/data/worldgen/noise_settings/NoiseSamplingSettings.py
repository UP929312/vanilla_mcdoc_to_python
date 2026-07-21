# Generated from symbols.json for ::java::data::worldgen::noise_settings::NoiseSamplingSettings
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class NoiseSamplingSettings:
    xz_scale: Annotated[float, 'Range | `0.001`-`1000` | both inclusive']
    y_scale: Annotated[float, 'Range | `0.001`-`1000` | both inclusive']
    xz_factor: Annotated[float, 'Range | `0.001`-`1000` | both inclusive']
    y_factor: Annotated[float, 'Range | `0.001`-`1000` | both inclusive']


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::noise_settings::NoiseSamplingSettings": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "xz_scale",
                "type": {
                    "kind": "double",
                    "valueRange": {
                        "kind": 0,
                        "min": 0.001,
                        "max": 1000
                    }
                }
            },
            {
                "kind": "pair",
                "key": "y_scale",
                "type": {
                    "kind": "double",
                    "valueRange": {
                        "kind": 0,
                        "min": 0.001,
                        "max": 1000
                    }
                }
            },
            {
                "kind": "pair",
                "key": "xz_factor",
                "type": {
                    "kind": "double",
                    "valueRange": {
                        "kind": 0,
                        "min": 0.001,
                        "max": 1000
                    }
                }
            },
            {
                "kind": "pair",
                "key": "y_factor",
                "type": {
                    "kind": "double",
                    "valueRange": {
                        "kind": 0,
                        "min": 0.001,
                        "max": 1000
                    }
                }
            }
        ]
    }
}

