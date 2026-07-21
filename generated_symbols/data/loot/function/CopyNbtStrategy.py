# Generated from symbols.json for ::java::data::loot::function::CopyNbtStrategy
from enum import Enum


class CopyNbtStrategy(Enum):
    REPLACE = "replace"  # Replace any existing contents of the target.
    APPEND = "append"  # Append to a list.
    MERGE = "merge"  # Merge into a compound tag.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::CopyNbtStrategy": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "desc": "Replace any existing contents of the target.",
                "identifier": "Replace",
                "value": "replace"
            },
            {
                "desc": "Append to a list.",
                "identifier": "Append",
                "value": "append"
            },
            {
                "desc": "Merge into a compound tag.",
                "identifier": "Merge",
                "value": "merge"
            }
        ]
    }
}

