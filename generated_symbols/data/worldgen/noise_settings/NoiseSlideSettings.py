"""
Generated from symbols.json for ::java::data::worldgen::noise_settings::NoiseSlideSettings
Local link to file: generated_symbols/data/worldgen/noise_settings/NoiseSlideSettings.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel


class NoiseSlideSettings(GeneratedModel):
    target: float  # The target density. Positive values add terrain and negative values remove terrain.
    size: Annotated[int, Field(ge=0, le=256)]  # Defines a range of 'Size * Size vertical * 4' blocks where the existing density and target are interpolated.
    offset: int  # Defines an range of 'Offset * Size vertical * 4' blocks where the density is set to the target.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::noise_settings::NoiseSlideSettings": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The target density. Positive values add terrain and negative values remove terrain.",
                "key": "target",
                "type": {
                    "kind": "float"
                }
            },
            {
                "kind": "pair",
                "desc": "Defines a range of 'Size * Size vertical * 4' blocks where the existing density and target are interpolated.",
                "key": "size",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 256
                    }
                }
            },
            {
                "kind": "pair",
                "desc": "Defines an range of 'Offset * Size vertical * 4' blocks where the density is set to the target.",
                "key": "offset",
                "type": {
                    "kind": "int"
                }
            }
        ]
    }
}
