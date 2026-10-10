"""
Generated from symbols.json for ::java::data::worldgen::structure::DimensionPaddingConfig
Local link to file: vanilla_mcdoc/data/worldgen/structure/DimensionPaddingConfig.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class DimensionPaddingConfig(GeneratedModel):
    bottom: Annotated[int, Field(ge=0)] | None = None
    top: Annotated[int, Field(ge=0)] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::structure::DimensionPaddingConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "bottom",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "top",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                },
                "optional": True
            }
        ]
    }
}
