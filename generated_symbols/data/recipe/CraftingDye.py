# Generated from symbols.json for ::java::data::recipe::CraftingDye
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.recipe.CraftingBookInfo import CraftingBookInfo
from generated_symbols.data.recipe.NotificationInfo import NotificationInfo

if TYPE_CHECKING:
    from generated_symbols.data.recipe.Ingredient import Ingredient
    from generated_symbols.world.item.ItemStackTemplate import ItemStackTemplate


@dataclass(kw_only=True)
class CraftingDye(NotificationInfo, CraftingBookInfo):
    target: Ingredient  # The item to be dyed.  Its `dyed_color` component will be dyed. The other components are copied.
    dye: Ingredient  # The items to provide dye color.  Colors are provided by the `dye` component.  Multiple dyes can be used at the same time.
    result: ItemStackTemplate


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::recipe::CraftingDye": {
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
                "desc": "The item to be dyed. \\\nIts `dyed_color` component will be dyed. The other components are copied.",
                "key": "target",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::recipe::Ingredient"
                }
            },
            {
                "kind": "pair",
                "desc": "The items to provide dye color. \\\nColors are provided by the `dye` component. \\\nMultiple dyes can be used at the same time.",
                "key": "dye",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::recipe::Ingredient"
                }
            },
            {
                "kind": "pair",
                "key": "result",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::item::ItemStackTemplate"
                }
            }
        ]
    }
}

