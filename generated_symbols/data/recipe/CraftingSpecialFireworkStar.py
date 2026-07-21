# Generated from symbols.json for ::java::data::recipe::CraftingSpecialFireworkStar
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.recipe.Ingredient import Ingredient
    from generated_symbols.world.component.item.FireworkShape import FireworkShape
    from generated_symbols.world.item.ItemStackTemplate import ItemStackTemplate


@dataclass(kw_only=True)
class CraftingSpecialFireworkStar:
    trail: Ingredient  # If this ingredient is provided, the result will have `has_trail` field set.
    twinkle: Ingredient  # If this ingredient is provided, the result will have `has_twinkle` field set.
    fuel: Ingredient  # Additional ingredient.  Exactly 1 additional ingredient is required.
    dye: Ingredient  # The items to provide explosion color.  Colors are provided by the `dye` component.  Multiple dyes can be used at the same time.
    shapes: dict[FireworkShape, Ingredient]  # If one of the ingredients is provided, the result will have the corresponding `shape` value.  If no shape ingredient is provided, the shape will be `small_ball`.
    result: ItemStackTemplate  # The `firework_explosion` component is controlled by the ingredients.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::recipe::CraftingSpecialFireworkStar": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "If this ingredient is provided, the result will have `has_trail` field set.",
                "key": "trail",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::recipe::Ingredient"
                }
            },
            {
                "kind": "pair",
                "desc": "If this ingredient is provided, the result will have `has_twinkle` field set.",
                "key": "twinkle",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::recipe::Ingredient"
                }
            },
            {
                "kind": "pair",
                "desc": "Additional ingredient. \\\nExactly 1 additional ingredient is required.",
                "key": "fuel",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::recipe::Ingredient"
                }
            },
            {
                "kind": "pair",
                "desc": "The items to provide explosion color. \\\nColors are provided by the `dye` component. \\\nMultiple dyes can be used at the same time.",
                "key": "dye",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::recipe::Ingredient"
                }
            },
            {
                "kind": "pair",
                "desc": "If one of the ingredients is provided, the result will have the corresponding `shape` value. \\\nIf no shape ingredient is provided, the shape will be `small_ball`.",
                "key": "shapes",
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": {
                                "kind": "reference",
                                "path": "::java::world::component::item::FireworkShape"
                            },
                            "type": {
                                "kind": "reference",
                                "path": "::java::data::recipe::Ingredient"
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "desc": "The `firework_explosion` component is controlled by the ingredients.",
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

