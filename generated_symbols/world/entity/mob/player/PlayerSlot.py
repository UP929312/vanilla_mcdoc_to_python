"""
Generated from symbols.json for ::java::world::entity::mob::player::PlayerSlot
Local link to file: generated_symbols/world/entity/mob/player/PlayerSlot.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field


type PlayerSlot = Annotated[int, Field(ge=0, le=35)]


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

