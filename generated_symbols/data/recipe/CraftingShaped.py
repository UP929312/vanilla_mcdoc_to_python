# Generated from symbols.json for ::java::data::recipe::CraftingShaped
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated
from generated_symbols.data.recipe.CraftingBookInfo import CraftingBookInfo
from generated_symbols.data.recipe.NotificationInfo import NotificationInfo

if TYPE_CHECKING:
    from generated_symbols.data.recipe.Ingredient import Ingredient
    from generated_symbols.world.item.ItemStackTemplate import ItemStackTemplate


@dataclass(kw_only=True)
class CraftingShaped(NotificationInfo, CraftingBookInfo):
    pattern: Annotated[list[Annotated[str, 'Length = 1-3 (both inclusive)']], 'Length = 1-3 (both inclusive)']
    key: dict[str, Ingredient]
    result: ItemStackTemplate


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::recipe::CraftingShaped": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.19.4"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "reference",
                    "path": "::java::data::recipe::NotificationInfo"
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::recipe::CraftingBookInfo"
                }
            },
            {
                "kind": "pair",
                "key": "pattern",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "string",
                        "lengthRange": {
                            "kind": 0,
                            "min": 1,
                            "max": 3
                        },
                        "attributes": [
                            {
                                "name": "crafting_ingredient",
                                "value": {
                                    "kind": "tree",
                                    "values": {
                                        "definition": {
                                            "kind": "literal",
                                            "value": {
                                                "kind": "boolean",
                                                "value": True
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 1,
                        "max": 3
                    }
                }
            },
            {
                "kind": "pair",
                "key": "key",
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": {
                                "kind": "string",
                                "attributes": [
                                    {
                                        "name": "crafting_ingredient"
                                    }
                                ]
                            },
                            "type": {
                                "kind": "reference",
                                "path": "::java::data::recipe::Ingredient"
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "result",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "reference",
                            "path": "::java::data::recipe::ItemResult",
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.20.5"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "reference",
                            "path": "::java::world::item::ItemStackTemplate",
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.20.5"
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                }
            }
        ]
    }
}

