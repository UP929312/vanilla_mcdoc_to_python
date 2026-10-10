"""
Generated from symbols.json for ::java::util::color::RGB
Local link to file: generated_symbols/util/color/RGB.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field


type RGB = int | tuple[Annotated[float, Field(ge=0, le=1)], Annotated[float, Field(ge=0, le=1)], Annotated[float, Field(ge=0, le=1)]]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::color::RGB": {
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
                                "value": "composite_rgb"
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
                    "min": 3,
                    "max": 3
                },
                "attributes": [
                    {
                        "name": "color",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "dec_rgb"
                            }
                        }
                    }
                ]
            }
        ]
    }
}
