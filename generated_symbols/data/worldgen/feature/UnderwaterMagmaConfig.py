"""
Generated from symbols.json for ::java::data::worldgen::feature::UnderwaterMagmaConfig
Local link to file: generated_symbols/data/worldgen/feature/UnderwaterMagmaConfig.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated, ClassVar


@dataclass(kw_only=True)
class UnderwaterMagmaConfig:
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

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

