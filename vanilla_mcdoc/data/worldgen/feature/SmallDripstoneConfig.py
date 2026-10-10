"""
Generated from symbols.json for ::java::data::worldgen::feature::SmallDripstoneConfig
Local link to file: generated_symbols/data/worldgen/feature/SmallDripstoneConfig.py
"""
# ~~~ CODE ~~~
from typing import Annotated, ClassVar

from pydantic import Field

from generated_symbols.base import GeneratedModel


class SmallDripstoneConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    max_placements: Annotated[int, Field(ge=0, le=100)] | None = None
    empty_space_search_radius: Annotated[int, Field(ge=0, le=20)] | None = None
    max_offset_from_origin: Annotated[int, Field(ge=0, le=20)] | None = None
    chance_of_taller_dripstone: Annotated[float, Field(ge=0, le=1)] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::SmallDripstoneConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "max_placements",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 100
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "empty_space_search_radius",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 20
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "max_offset_from_origin",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 20
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "chance_of_taller_dripstone",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1
                    }
                },
                "optional": True
            }
        ]
    }
}
