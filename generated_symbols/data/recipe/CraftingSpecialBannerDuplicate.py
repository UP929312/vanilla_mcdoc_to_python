# Generated from symbols.json for ::java::data::recipe::CraftingSpecialBannerDuplicate
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.recipe.Ingredient import Ingredient
    from generated_symbols.world.item.ItemStackTemplate import ItemStackTemplate


@dataclass(kw_only=True)
class CraftingSpecialBannerDuplicate:
    banner: Ingredient  # The banner item. The item type is required to be `BannerItem`.  Exactly 2 banners of the same color are required.  The one with patterns is viewed as "source". Its components will be copied.  The other is viewed as "target". It is required to have no patterns.   The source banner will be kept in the crafting grid.
    result: ItemStackTemplate


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::recipe::CraftingSpecialBannerDuplicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The banner item. The item type is required to be `BannerItem`. \\\nExactly 2 banners of the same color are required. \\\nThe one with patterns is viewed as \"source\". Its components will be copied. \\\nThe other is viewed as \"target\". It is required to have no patterns. \\\n\\\nThe source banner will be kept in the crafting grid.",
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

