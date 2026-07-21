# Generated from symbols.json for ::java::util::color::StringRGB
from typing import Annotated


type StringRGB = int | tuple[Annotated[float, 'Range | `0`-`1` | both inclusive'], Annotated[float, 'Range | `0`-`1` | both inclusive'], Annotated[float, 'Range | `0`-`1` | both inclusive']] | str


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

