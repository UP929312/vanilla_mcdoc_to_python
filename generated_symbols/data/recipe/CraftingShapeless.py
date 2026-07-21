# Generated from symbols.json for ::java::data::recipe::CraftingShapeless
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated
from generated_symbols.data.recipe.CraftingBookInfo import CraftingBookInfo
from generated_symbols.data.recipe.NotificationInfo import NotificationInfo

if TYPE_CHECKING:
    from generated_symbols.data.recipe.Ingredient import Ingredient
    from generated_symbols.world.item.ItemStackTemplate import ItemStackTemplate


@dataclass(kw_only=True)
class CraftingShapeless(NotificationInfo, CraftingBookInfo):
    ingredients: Annotated[list[Ingredient], 'Length = 1-9 (both inclusive)']
    result: ItemStackTemplate


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::recipe::CraftingShapeless": {
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
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::recipe::CraftingBookInfo"
                }
            },
            {
                "kind": "pair",
                "key": "ingredients",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::recipe::Ingredient"
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 1,
                        "max": 9
                    }
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

