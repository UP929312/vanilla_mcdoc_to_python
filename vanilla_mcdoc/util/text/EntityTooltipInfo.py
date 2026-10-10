"""
Generated from symbols.json for ::java::util::text::EntityTooltipInfo
Local link to file: vanilla_mcdoc/util/text/EntityTooltipInfo.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec, MinecraftUUID, MinecraftUUIDString

if TYPE_CHECKING:
    from vanilla_mcdoc.util.text.Text import Text


class EntityTooltipInfo(GeneratedModel):
    id: Annotated[str, IdSpec(registry='entity_type')]
    uuid: MinecraftUUID | MinecraftUUIDString
    name: Text | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::text::EntityTooltipInfo": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "id",
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
                "key": "uuid",
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
