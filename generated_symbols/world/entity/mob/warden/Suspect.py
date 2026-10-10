"""
Generated from symbols.json for ::java::world::entity::mob::warden::Suspect
Local link to file: generated_symbols/world/entity/mob/warden/Suspect.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel
from generated_symbols.minecraft_types import MinecraftUUID


class Suspect(GeneratedModel):
    anger: Annotated[int, Field(ge=1, le=150)] | None = None  # Level of anger that will decrease by 1 every second.
    uuid: MinecraftUUID | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::warden::Suspect": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Level of anger that will decrease by 1 every second.",
                "key": "anger",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1,
                        "max": 150
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "uuid",
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
            }
        ]
    }
}

