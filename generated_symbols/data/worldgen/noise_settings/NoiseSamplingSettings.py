"""
Generated from symbols.json for ::java::data::worldgen::noise_settings::NoiseSamplingSettings
Local link to file: generated_symbols/data/worldgen/noise_settings/NoiseSamplingSettings.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel


class NoiseSamplingSettings(GeneratedModel):
    xz_scale: Annotated[float, Field(ge=0.001, le=1000)]
    y_scale: Annotated[float, Field(ge=0.001, le=1000)]
    xz_factor: Annotated[float, Field(ge=0.001, le=1000)]
    y_factor: Annotated[float, Field(ge=0.001, le=1000)]


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

