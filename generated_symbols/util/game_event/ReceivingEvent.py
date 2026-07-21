# Generated from symbols.json for ::java::util::game_event::ReceivingEvent
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class ReceivingEvent:
    game_event: str
    distance: Annotated[float, 'Range | Min `0` and above | inclusive']  # Distance in blocks to the source
    pos: tuple[float, float, float]  # Origin of the event
    source: tuple[int, int, int, int] | None = None  # UUID of the source entity of the event, if one exists
    projectile_owner: tuple[int, int, int, int] | None = None  # UUID of the owner of the projectile, if one exists


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::game_event::ReceivingEvent": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "game_event",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "game_event"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "desc": "Distance in blocks to the source",
                "key": "distance",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                }
            },
            {
                "kind": "pair",
                "desc": "Origin of the event",
                "key": "pos",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "float"
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 3,
                        "max": 3
                    }
                }
            },
            {
                "kind": "pair",
                "desc": "UUID of the source entity of the event, if one exists",
                "key": "source",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "int"
                    },
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
                "desc": "UUID of the owner of the projectile, if one exists",
                "key": "projectile_owner",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "int"
                    },
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
            }
        ]
    }
}

