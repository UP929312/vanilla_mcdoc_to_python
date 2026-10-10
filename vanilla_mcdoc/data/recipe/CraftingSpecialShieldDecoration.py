"""
Generated from symbols.json for ::java::data::recipe::CraftingSpecialShieldDecoration
Local link to file: vanilla_mcdoc/data/recipe/CraftingSpecialShieldDecoration.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.recipe.Ingredient import Ingredient
    from vanilla_mcdoc.world.item.ItemStackTemplate import ItemStackTemplate


class CraftingSpecialShieldDecoration(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'recipe'

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
