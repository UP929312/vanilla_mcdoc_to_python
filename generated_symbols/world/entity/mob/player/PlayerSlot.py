# Generated from symbols.json for ::java::world::entity::mob::player::PlayerSlot
from typing import Annotated


type PlayerSlot = Annotated[int, 'Range | `0`-`35` | both inclusive']


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::player::PlayerSlot": {
        "kind": "union",
        "members": [
            {
                "kind": "byte",
                "valueRange": {
                    "kind": 0,
                    "min": 0,
                    "max": 35
                }
            },
            {
                "kind": "byte",
                "valueRange": {
                    "kind": 0,
                    "min": 100,
                    "max": 103
                },
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.5"
                            }
                        }
                    }
                ]
            },
            {
                "kind": "byte",
                "valueRange": {
                    "kind": 0,
                    "min": -106,
                    "max": -106
                },
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.5"
                            }
                        }
                    }
                ]
            }
        ]
    }
}

