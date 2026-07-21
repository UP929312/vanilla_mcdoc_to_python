# Generated from symbols.json for ::java::data::recipe::CraftingSpecialMapExtending
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.recipe.Ingredient import Ingredient
    from generated_symbols.world.item.ItemStackTemplate import ItemStackTemplate


@dataclass(kw_only=True)
class CraftingSpecialMapExtending:
    map: Ingredient  # The map item.  The `map_id` component is used to determine the resulting item.  The other components are copied.  This item is placed at the center grid.   The source map will be kept in the crafting grid.
    material: Ingredient  # Additional ingredients.  8 `material` items are required to surroud the `map` item.
    result: ItemStackTemplate  # The previewing result will have `map_post_processing` transient component.  The crafted result will have a new `map_id` component, which shows the extended version of the original map.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::recipe::CraftingSpecialMapExtending": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The map item. \\\nThe `map_id` component is used to determine the resulting item. \\\nThe other components are copied. \\\nThis item is placed at the center grid. \\\n\\\nThe source map will be kept in the crafting grid.",
                "key": "map",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::recipe::Ingredient"
                }
            },
            {
                "kind": "pair",
                "desc": "Additional ingredients. \\\n8 `material` items are required to surroud the `map` item.",
                "key": "material",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::recipe::Ingredient"
                }
            },
            {
                "kind": "pair",
                "desc": "The previewing result will have `map_post_processing` transient component. \\\nThe crafted result will have a new `map_id` component, which shows the extended version of the original map.",
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

