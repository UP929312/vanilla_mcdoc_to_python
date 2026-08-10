"""
Generated from symbols.json for ::java::world::block::beacon::NoneId
Local link to file: generated_symbols/world/block/beacon/NoneId.py
"""
# ~~~ CODE ~~~
from typing import Literal


type NoneId = Literal[-1]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::beacon::NoneId": {
        "kind": "union",
        "members": [
            {
                "kind": "literal",
                "value": {
                    "kind": "int",
                    "value": 0
                },
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.16"
                            }
                        }
                    }
                ]
            },
            {
                "kind": "literal",
                "value": {
                    "kind": "int",
                    "value": -1
                },
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.16"
                            }
                        }
                    }
                ]
            }
        ]
    }
}

