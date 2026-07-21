# Generated from symbols.json for ::java::data::recipe::Brewing
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.recipe.PotionIngredient import PotionIngredient
    from generated_symbols.world.item.ItemStackTemplate import ItemStackTemplate


@dataclass(kw_only=True)
class Brewing:
    input: PotionIngredient  # The original potion.
    reagent: PotionIngredient  # The ingredient.
    output: ItemStackTemplate


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::recipe::Brewing": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The original potion.",
                "key": "input",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::recipe::PotionIngredient"
                }
            },
            {
                "kind": "pair",
                "desc": "The ingredient.",
                "key": "reagent",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::recipe::PotionIngredient"
                }
            },
            {
                "kind": "pair",
                "key": "output",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::item::ItemStackTemplate"
                }
            }
        ]
    }
}

