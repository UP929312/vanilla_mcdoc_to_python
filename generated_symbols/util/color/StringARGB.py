# Generated from symbols.json for ::java::util::color::StringARGB
from typing import Annotated


type StringARGB = int | tuple[Annotated[float, 'Range | `0`-`1` | both inclusive'], Annotated[float, 'Range | `0`-`1` | both inclusive'], Annotated[float, 'Range | `0`-`1` | both inclusive'], Annotated[float, 'Range | `0`-`1` | both inclusive']] | str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::color::StringARGB": {
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
                                "value": "hex_argb"
                            }
                        }
                    }
                ]
            }
        ]
    }
}

