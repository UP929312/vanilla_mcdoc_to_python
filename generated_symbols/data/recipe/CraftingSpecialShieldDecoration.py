# Generated from symbols.json for ::java::data::recipe::CraftingSpecialShieldDecoration
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.recipe.Ingredient import Ingredient
    from generated_symbols.world.item.ItemStackTemplate import ItemStackTemplate


@dataclass(kw_only=True)
class CraftingSpecialShieldDecoration:
    target: Ingredient  # The item to be decorated. It is required to have no patterns.  Its components, except `base_color` and `banner_patterns`, are copied.
    banner: Ingredient  # The banner item. The item type is required to be `BannerItem`.  Determines the `base_color` component of the resulting item.
    result: ItemStackTemplate


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::recipe::CraftingSpecialShieldDecoration": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The item to be decorated. It is required to have no patterns. \\\nIts components, except `base_color` and `banner_patterns`, are copied.",
                "key": "target",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::recipe::Ingredient"
                }
            },
            {
                "kind": "pair",
                "desc": "The banner item. The item type is required to be `BannerItem`. \\\nDetermines the `base_color` component of the resulting item.",
                "key": "banner",
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
        ],
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
        ]
    }
}

