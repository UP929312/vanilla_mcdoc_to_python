"""
Generated from symbols.json for ::java::util::color::RGBA
Local link to file: vanilla_mcdoc/util/color/RGBA.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field


type RGBA = int | tuple[Annotated[float, Field(ge=0, le=1)], Annotated[float, Field(ge=0, le=1)], Annotated[float, Field(ge=0, le=1)], Annotated[float, Field(ge=0, le=1)]]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::color::RGBA": {
        "kind": "union",
        "members": [
            {
                "kind": "int",
                "attributes": [
                    {
                        "name": "canonical"
                    },
                    {
                        "name": "color",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "composite_argb"
                            }
                        }
                    }
                ]
            },
            {
                "kind": "list",
                "item": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1
                    }
                },
                "lengthRange": {
                    "kind": 0,
                    "min": 4,
                    "max": 4
                },
                "attributes": [
                    {
                        "name": "color",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "dec_rgba"
                            }
                        }
                    }
                ]
            }
        ]
    }
}
