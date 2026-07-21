# Generated from symbols.json for ::java::util::color::RGB
from typing import Annotated


type RGB = int | tuple[Annotated[float, 'Range | `0`-`1` | both inclusive'], Annotated[float, 'Range | `0`-`1` | both inclusive'], Annotated[float, 'Range | `0`-`1` | both inclusive']]


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

