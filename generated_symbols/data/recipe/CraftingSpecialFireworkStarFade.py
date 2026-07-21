# Generated from symbols.json for ::java::data::recipe::CraftingSpecialFireworkStarFade
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.recipe.Ingredient import Ingredient
    from generated_symbols.world.item.ItemStackTemplate import ItemStackTemplate


@dataclass(kw_only=True)
class CraftingSpecialFireworkStarFade:
    target: Ingredient  # The firework star item.  The fade effect of its `firework_explosion` will be changed.  The other components are copied.
    dye: Ingredient  # The items to provide fade color.  Colors are provided by the `dye` component.  Multiple dyes can be used at the same time.
    result: ItemStackTemplate


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::recipe::CraftingSpecialFireworkStarFade": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The firework star item. \\\nThe fade effect of its `firework_explosion` will be changed. \\\nThe other components are copied.",
                "key": "target",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::recipe::Ingredient"
                }
            },
            {
                "kind": "pair",
                "desc": "The items to provide fade color. \\\nColors are provided by the `dye` component. \\\nMultiple dyes can be used at the same time.",
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

