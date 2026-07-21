# Generated from symbols.json for ::java::assets::item_definition::Chest
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.assets.item_definition.ChestType import ChestType


@dataclass(kw_only=True)
class Chest:
    texture: str
    openness: Annotated[float, 'Range | `0`-`1` | both inclusive'] | None = None  # Defaults to `0`.
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

