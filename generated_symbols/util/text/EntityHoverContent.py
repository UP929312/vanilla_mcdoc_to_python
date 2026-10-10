"""
Generated from symbols.json for ::java::util::text::EntityHoverContent
Local link to file: generated_symbols/util/text/EntityHoverContent.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from generated_symbols.base import GeneratedModel
from generated_symbols.minecraft_types import MinecraftUUID, MinecraftUUIDString
from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.util.text.Text import Text


class EntityHoverContent(GeneratedModel):
    type: Annotated[str, IdSpec(registry='entity_type')]
    id: MinecraftUUID | MinecraftUUIDString
    name: Text | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::text::EntityHoverContent": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "entity_type"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "id",
                "type": {
                    "kind": "union",
                    "members": [
                        {
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
                                    "name": "canonical"
                                }
                            ]
                        },
                        {
                            "kind": "string"
                        }
                    ],
                    "attributes": [
                        {
                            "name": "uuid"
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "name",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::text::Text"
                },
                "optional": True
            }
        ]
    }
}

