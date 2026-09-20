"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::ThreeLayersFeatureSize
Local link to file: generated_symbols/data/worldgen/feature/tree/ThreeLayersFeatureSize.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from generated_symbols.base import GeneratedModel
from pydantic import Field


class ThreeLayersFeatureSize(GeneratedModel):
    min_clipped_height: Annotated[float, Field(ge=0, le=80)] | None = None
    limit: Annotated[int, Field(ge=0, le=80)] | None = None
    upper_limit: Annotated[int, Field(ge=0, le=80)] | None = None
    lower_size: Annotated[int, Field(ge=0, le=16)] | None = None
    middle_size: Annotated[int, Field(ge=0, le=16)] | None = None
    upper_size: Annotated[int, Field(ge=0, le=16)] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::tree::ThreeLayersFeatureSize": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "min_clipped_height",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 80
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "limit",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 80
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "upper_limit",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 80
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "lower_size",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 16
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "middle_size",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 16
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "upper_size",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 16
                    }
                },
                "optional": True
            }
        ]
    }
}

