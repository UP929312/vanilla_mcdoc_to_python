# Generated from symbols.json for ::java::data::worldgen::attribute::TriState
from typing import Literal


type TriState = bool | Literal['default']


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::attribute::TriState": {
        "kind": "union",
        "members": [
            {
                "kind": "boolean"
            },
            {
                "kind": "literal",
                "value": {
                    "kind": "string",
                    "value": "default"
                }
            }
        ]
    }
}

