# Generated from symbols.json for ::java::world::entity::interaction::Action
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class Action:
    player: tuple[int, int, int, int] | None = None
    timestamp: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # Game tick of when the event occured.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::interaction::Action": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "player",
                "type": {
                    "kind": "int_array",
                    "lengthRange": {
                        "kind": 0,
                        "min": 4,
                        "max": 4
                    },
                    "attributes": [
                        {
                            "name": "uuid"
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Game tick of when the event occured.",
                "key": "timestamp",
                "type": {
                    "kind": "long",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                },
                "optional": True
            }
        ]
    }
}

