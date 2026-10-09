"""
Generated from symbols.json for ::java::util::color::StringRGB
Local link to file: generated_symbols/util/color/StringRGB.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field


type StringRGB = int | tuple[Annotated[float, Field(ge=0, le=1)], Annotated[float, Field(ge=0, le=1)], Annotated[float, Field(ge=0, le=1)]] | Annotated[str, Field(pattern='^#')]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::color::StringRGB": {
        "kind": "union",
        "members": [
            {
                "kind": "int",
                "attributes": [
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
            },
            {
                "kind": "string",
                "attributes": [
                    {
                        "name": "color",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "hex_rgb"
                            }
                        }
                    }
                ]
            }
        ]
    }
}

