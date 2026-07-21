# Generated from symbols.json for ::java::data::recipe::CraftingImbue
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.recipe.CraftingBookInfo import CraftingBookInfo
from generated_symbols.data.recipe.NotificationInfo import NotificationInfo

if TYPE_CHECKING:
    from generated_symbols.data.recipe.Ingredient import Ingredient
    from generated_symbols.world.item.ItemStackTemplate import ItemStackTemplate


@dataclass(kw_only=True)
class CraftingImbue(NotificationInfo, CraftingBookInfo):
    source: Ingredient  # The item to provide potion effect.  Its `potion_contents` component will be copied.  This item is placed at the center grid.
    material: Ingredient  # Additional ingredients.  8 `material` items are required to surroud the `source` item.
    result: ItemStackTemplate


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::recipe::CraftingImbue": {
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
                "desc": "The item to provide potion effect. \\\nIts `potion_contents` component will be copied. \\\nThis item is placed at the center grid.",
                "key": "source",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::recipe::Ingredient"
                }
            },
            {
                "kind": "pair",
                "desc": "Additional ingredients. \\\n8 `material` items are required to surroud the `source` item.",
                "key": "material",
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

