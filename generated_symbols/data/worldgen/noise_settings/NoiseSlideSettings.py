# Generated from symbols.json for ::java::data::worldgen::noise_settings::NoiseSlideSettings
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class NoiseSlideSettings:
    target: float  # The target density. Positive values add terrain and negative values remove terrain.
    size: Annotated[int, 'Range | `0`-`256` | both inclusive']  # Defines a range of 'Size * Size vertical * 4' blocks where the existing density and target are interpolated.
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

