"""
Generated from symbols.json for ::java::data::worldgen::structure::JigsawDistanceLimits
Local link to file: vanilla_mcdoc/data/worldgen/structure/JigsawDistanceLimits.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Generic, TypeVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


T = TypeVar('T')


class JigsawDistanceLimits(GeneratedModel, Generic[T]):
    horizontal: T
    vertical: Annotated[int, Field(ge=1, le=4064)] | None = None  # Defaults to 4064


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::structure::JigsawDistanceLimits": {
        "kind": "template",
        "child": {
            "kind": "struct",
            "fields": [
                {
                    "kind": "pair",
                    "key": "horizontal",
                    "type": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::structure::T"
                    }
                },
                {
                    "kind": "pair",
                    "desc": "Defaults to 4064",
                    "key": "vertical",
                    "type": {
                        "kind": "int",
                        "valueRange": {
                            "kind": 0,
                            "min": 1,
                            "max": 4064
                        }
                    },
                    "optional": True
                }
            ]
        },
        "typeParams": [
            {
                "path": "::java::data::worldgen::structure::T"
            }
        ]
    }
}
