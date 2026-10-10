"""
Generated from symbols.json for ::java::world::entity::interaction::Action
Local link to file: generated_symbols/world/entity/interaction/Action.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel
from generated_symbols.minecraft_types import MinecraftUUID


class Action(GeneratedModel):
    player: MinecraftUUID | None = None
    timestamp: Annotated[int, Field(ge=0)] | None = None  # Game tick of when the event occured.


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
