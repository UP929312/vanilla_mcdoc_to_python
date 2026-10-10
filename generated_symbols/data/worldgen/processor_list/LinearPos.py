"""
Generated from symbols.json for ::java::data::worldgen::processor_list::LinearPos
Local link to file: generated_symbols/data/worldgen/processor_list/LinearPos.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel


class LinearPos(GeneratedModel):
    min_dist: Annotated[int, Field(ge=0, le=255)] | None = None
    max_dist: Annotated[int, Field(ge=0, le=255)] | None = None
    min_chance: Annotated[float, Field(ge=0, le=1)] | None = None
    max_chance: Annotated[float, Field(ge=0, le=1)] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::processor_list::LinearPos": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "min_dist",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 255
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "max_dist",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 255
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "min_chance",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "max_chance",
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

