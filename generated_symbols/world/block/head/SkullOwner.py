"""
Generated from symbols.json for ::java::world::block::head::SkullOwner
Local link to file: generated_symbols/world/block/head/SkullOwner.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from pydantic import Field

from generated_symbols.base import GeneratedModel
from generated_symbols.minecraft_types import MinecraftUUID

if TYPE_CHECKING:
    from generated_symbols.world.block.head.Properties import Properties


class SkullOwner(GeneratedModel):
    Id: MinecraftUUID | None = None  # Optional.
    Name: str | None = None  # Name of the owner, if missing appears as a steve head.
    Properties_: Properties | None = Field(default=None, alias='Properties')


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::head::SkullOwner": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Optional.",
                "key": "Id",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.16"
                                        }
                                    }
                                },
                                {
                                    "name": "uuid"
                                }
                            ]
                        },
                        {
                            "kind": "int_array",
                            "lengthRange": {
                                "kind": 0,
                                "min": 4,
                                "max": 4
                            },
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.16"
                                        }
                                    }
                                },
                                {
                                    "name": "uuid"
                                }
                            ]
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Name of the owner, if missing appears as a steve head.",
                "key": "Name",
                "type": {
                    "kind": "string"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "Properties",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::block::head::Properties"
                },
                "optional": True
            }
        ]
    }
}

