# Generated from symbols.json for ::java::data::recipe::SmithingTransform
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.recipe.NotificationInfo import NotificationInfo

if TYPE_CHECKING:
    from generated_symbols.data.recipe.Ingredient import Ingredient
    from generated_symbols.world.item.ItemStackTemplate import ItemStackTemplate


@dataclass(kw_only=True)
class SmithingTransform(NotificationInfo):
    base: Ingredient  # Ingredient specifying an item to be transformed.
    result: ItemStackTemplate  # Resulting transformed item.
    addition: Ingredient | None = None  # Material that will be used.
    template: Ingredient | None = None  # Template item that will be used for the pattern.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::recipe::SmithingTransform": {
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
                                "value": "26.1"
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
                "kind": "pair",
                "attributes": [
                    {
                        "name": "deprecated"
                    },
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.1"
                            }
                        }
                    }
                ],
                "desc": "This field is unused by the game.",
                "key": "group",
                "type": {
                    "kind": "string"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Ingredient specifying an item to be transformed.",
                "key": "base",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::recipe::Ingredient"
                }
            },
            {
                "kind": "spread",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.2"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "desc": "Material that will be used.",
                            "key": "addition",
                            "type": {
                                "kind": "reference",
                                "path": "::java::data::recipe::Ingredient"
                            }
                        },
                        {
                            "kind": "pair",
                            "desc": "Template item that will be used for the pattern.",
                            "key": "template",
                            "type": {
                                "kind": "reference",
                                "path": "::java::data::recipe::Ingredient"
                            }
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.2"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "desc": "Material that will be used.",
                            "key": "addition",
                            "type": {
                                "kind": "reference",
                                "path": "::java::data::recipe::Ingredient"
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "desc": "Template item that will be used for the pattern.",
                            "key": "template",
                            "type": {
                                "kind": "reference",
                                "path": "::java::data::recipe::Ingredient"
                            },
                            "optional": True
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "desc": "Resulting transformed item.",
                "key": "result",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "struct",
                            "fields": [
                                {
                                    "kind": "pair",
                                    "key": "item",
                                    "type": {
                                        "kind": "string",
                                        "attributes": [
                                            {
                                                "name": "id",
                                                "value": {
                                                    "kind": "literal",
                                                    "value": {
                                                        "kind": "string",
                                                        "value": "item"
                                                    }
                                                }
                                            }
                                        ]
                                    }
                                }
                            ],
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

