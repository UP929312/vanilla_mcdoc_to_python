# Generated from symbols.json for ::java::data::recipe::CraftingSpecialFireworkRocket
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.recipe.Ingredient import Ingredient
    from generated_symbols.world.item.ItemStackTemplate import ItemStackTemplate


@dataclass(kw_only=True)
class CraftingSpecialFireworkRocket:
    shell: Ingredient  # Additional ingredient.  Exactly 1 additional ingredient is required.
    fuel: Ingredient  # The fuel ingredient.  The count of fuel ingredients controls the `flight_duration` field.  Only 1 ~ 3 fuels are allowed.
    star: Ingredient  # The firework star ingredient.  Provides explosion data by the `firework_explosion` component.  Any count of stars (including 0) are allowed.
    result: ItemStackTemplate  # The `fireworks` component is controlled by `fuel` and `star`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::recipe::CraftingSpecialFireworkRocket": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Additional ingredient. \\\nExactly 1 additional ingredient is required.",
                "key": "shell",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::recipe::Ingredient"
                }
            },
            {
                "kind": "pair",
                "desc": "The fuel ingredient. \\\nThe count of fuel ingredients controls the `flight_duration` field. \\\nOnly 1 ~ 3 fuels are allowed.",
                "key": "fuel",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::recipe::Ingredient"
                }
            },
            {
                "kind": "pair",
                "desc": "The firework star ingredient. \\\nProvides explosion data by the `firework_explosion` component. \\\nAny count of stars (including 0) are allowed.",
                "key": "star",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::recipe::Ingredient"
                }
            },
            {
                "kind": "pair",
                "desc": "The `fireworks` component is controlled by `fuel` and `star`.",
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

