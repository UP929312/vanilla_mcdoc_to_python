"""
Generated from symbols.json for ::java::util::game_event::EntityPositionSource
Local link to file: vanilla_mcdoc/util/game_event/EntityPositionSource.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import MinecraftUUID


class EntityPositionSource(GeneratedModel):
    source_entity: MinecraftUUID
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
