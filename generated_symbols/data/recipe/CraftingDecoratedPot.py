"""
Generated from symbols.json for ::java::data::recipe::CraftingDecoratedPot
Local link to file: generated_symbols/data/recipe/CraftingDecoratedPot.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.recipe.Ingredient import Ingredient
    from generated_symbols.world.item.ItemStackTemplate import ItemStackTemplate


class CraftingDecoratedPot(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'recipe'

    back: Ingredient
    left: Ingredient
    right: Ingredient
    front: Ingredient
    result: ItemStackTemplate  # The `pot_decorations` component will store the 4 ingredients.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::recipe::CraftingDecoratedPot": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "back",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::recipe::Ingredient"
                }
            },
            {
                "kind": "pair",
                "key": "left",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::recipe::Ingredient"
                }
            },
            {
                "kind": "pair",
                "key": "right",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::recipe::Ingredient"
                }
            },
            {
                "kind": "pair",
                "key": "front",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::recipe::Ingredient"
                }
            },
            {
                "kind": "pair",
                "desc": "The `pot_decorations` component will store the 4 ingredients.",
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

