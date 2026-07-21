# Generated from symbols.json for ::java::util::game_event::EntityPositionSource
from dataclasses import dataclass


@dataclass(kw_only=True)
class EntityPositionSource:
    source_entity: tuple[int, int, int, int]
    y_offset: float | None = None  # offset from the entity's feet to the source position


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::game_event::EntityPositionSource": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "source_entity",
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
                }
            },
            {
                "kind": "pair",
                "desc": "offset from the entity's feet to the source position",
                "key": "y_offset",
                "type": {
                    "kind": "float"
                },
                "optional": True
            }
        ]
    }
}

