"""
Generated from symbols.json for ::java::pack::PackFormat
Local link to file: vanilla_mcdoc/pack/PackFormat.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field


type PackFormat = int | tuple[int] | tuple[int, Annotated[int, Field(ge=0)]]


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
