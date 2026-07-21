# Generated from symbols.json for ::java::pack::PackFormat
from typing import Annotated


type PackFormat = int | tuple[int] | tuple[int, Annotated[int, 'Range | Min `0` and above | inclusive']]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::pack::PackFormat": {
        "kind": "union",
        "members": [
            {
                "kind": "int"
            },
            {
                "kind": "list",
                "item": {
                    "kind": "int"
                },
                "lengthRange": {
                    "kind": 0,
                    "min": 1,
                    "max": 1
                }
            },
            {
                "kind": "tuple",
                "items": [
                    {
                        "kind": "int"
                    },
                    {
                        "kind": "int",
                        "valueRange": {
                            "kind": 0,
                            "min": 0
                        }
                    }
                ]
            }
        ]
    }
}

