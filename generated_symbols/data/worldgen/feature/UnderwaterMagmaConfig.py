"""
Generated from symbols.json for ::java::data::worldgen::feature::UnderwaterMagmaConfig
Local link to file: generated_symbols/data/worldgen/feature/UnderwaterMagmaConfig.py
"""
# ~~~ CODE ~~~
from typing import Annotated, ClassVar

from pydantic import Field

from generated_symbols.base import GeneratedModel


class UnderwaterMagmaConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    floor_search_range: Annotated[int, Field(ge=0, le=512)]
    placement_radius_around_floor: Annotated[int, Field(ge=0, le=64)]
    placement_probability_per_valid_position: Annotated[float, Field(ge=0, le=1)]


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

