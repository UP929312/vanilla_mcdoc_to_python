# Generated from symbols.json for ::java::data::worldgen::attribute::modifier::ListModifierType
from enum import Enum


class ListModifierType(Enum):
    OVERRIDE = "override"
    APPEND = "append"


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::attribute::modifier::ListModifierType": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "identifier": "Override",
                "value": "override"
            },
            {
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "identifier": "Append",
                "value": "append"
            }
        ]
    }
}

