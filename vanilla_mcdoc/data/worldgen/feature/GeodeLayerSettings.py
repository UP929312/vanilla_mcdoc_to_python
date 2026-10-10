"""
Generated from symbols.json for ::java::data::worldgen::feature::GeodeLayerSettings
Local link to file: vanilla_mcdoc/data/worldgen/feature/GeodeLayerSettings.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class GeodeLayerSettings(GeneratedModel):
    filling: Annotated[float, Field(ge=0.01, le=50)] | None = None
    inner_layer: Annotated[float, Field(ge=0.01, le=50)] | None = None
    middle_layer: Annotated[float, Field(ge=0.01, le=50)] | None = None
    outer_layer: Annotated[float, Field(ge=0.01, le=50)] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::GeodeLayerSettings": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "filling",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0.01,
                        "max": 50
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "inner_layer",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0.01,
                        "max": 50
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "middle_layer",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0.01,
                        "max": 50
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "outer_layer",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0.01,
                        "max": 50
                    }
                },
                "optional": True
            }
        ]
    }
}
