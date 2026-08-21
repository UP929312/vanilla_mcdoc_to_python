"""
Generated from symbols.json for ::java::data::loot::function::ListOperationMode
Local link to file: generated_symbols/data/loot/function/ListOperationMode.py
"""
# ~~~ CODE ~~~
from enum import StrEnum


class ListOperationMode(StrEnum):
    APPEND = "append"
    INSERT = "insert"
    REPLACEALL = "replace_all"
    REPLACESECTION = "replace_section"


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::ListOperationMode": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "identifier": "Append",
                "value": "append"
            },
            {
                "identifier": "Insert",
                "value": "insert"
            },
            {
                "identifier": "ReplaceAll",
                "value": "replace_all"
            },
            {
                "identifier": "ReplaceSection",
                "value": "replace_section"
            }
        ]
    }
}

