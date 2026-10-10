"""
Generated from symbols.json for ::java::assets::item_definition::Chest
Local link to file: generated_symbols/assets/item_definition/Chest.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel
from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.assets.item_definition.ChestType import ChestType


class Chest(GeneratedModel):
    texture: Annotated[str, IdSpec(registry='texture', path='entity/chest/')]
    openness: Annotated[float, Field(ge=0, le=1)] | None = None  # Defaults to `0`.
    chest_type: ChestType | None = None  # Defaults to `single`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::Chest": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "texture",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "tree",
                                "values": {
                                    "registry": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "texture"
                                        }
                                    },
                                    "path": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "entity/chest/"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "desc": "Defaults to `0`.",
                "key": "openness",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.1"
                            }
                        }
                    }
                ],
                "desc": "Defaults to `single`.",
                "key": "chest_type",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::item_definition::ChestType"
                },
                "optional": True
            }
        ]
    }
}
