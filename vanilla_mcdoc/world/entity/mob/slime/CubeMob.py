"""
Generated from symbols.json for ::java::world::entity::mob::slime::CubeMob
Local link to file: generated_symbols/world/entity/mob/slime/CubeMob.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel


class CubeMob(GeneratedModel):
    Size: Annotated[int, Field(ge=0, le=126)] | None = None
    wasOnGround: bool | None = None  # Whether it is on the ground.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::slime::CubeMob": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "Size",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "int",
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.17"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "int",
                            "valueRange": {
                                "kind": 0,
                                "min": 0,
                                "max": 126
                            },
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.17"
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether it is on the ground.",
                "key": "wasOnGround",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}
