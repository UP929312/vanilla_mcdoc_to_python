# Generated from symbols.json for ::java::data::worldgen::feature::UnderwaterMagmaConfig
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class UnderwaterMagmaConfig:
    floor_search_range: Annotated[int, 'Range | `0`-`512` | both inclusive']
    placement_radius_around_floor: Annotated[int, 'Range | `0`-`64` | both inclusive']
    placement_probability_per_valid_position: Annotated[float, 'Range | `0`-`1` | both inclusive']


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::UnderwaterMagmaConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "floor_search_range",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 512
                    }
                }
            },
            {
                "kind": "pair",
                "key": "placement_radius_around_floor",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 64
                    }
                }
            },
            {
                "kind": "pair",
                "key": "placement_probability_per_valid_position",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1
                    }
                }
            }
        ]
    }
}

