"""
Generated from symbols.json for ::java::data::recipe::CraftingDecoratedPot
Local link to file: vanilla_mcdoc/data/recipe/CraftingDecoratedPot.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.recipe.Ingredient import Ingredient
    from vanilla_mcdoc.world.item.ItemStackTemplate import ItemStackTemplate


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
