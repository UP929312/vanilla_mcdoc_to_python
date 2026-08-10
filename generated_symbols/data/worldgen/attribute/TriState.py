"""
Generated from symbols.json for ::java::data::worldgen::attribute::TriState
Local link to file: generated_symbols/data/worldgen/attribute/TriState.py
"""
# ~~~ CODE ~~~
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

