# Generated from symbols.json for ::java::world::entity::mob::slime::CubeMob
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class CubeMob:
    Size: Annotated[int, 'Range | `0`-`126` | both inclusive'] | None = None
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

