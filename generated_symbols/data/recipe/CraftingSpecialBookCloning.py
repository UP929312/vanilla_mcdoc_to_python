# Generated from symbols.json for ::java::data::recipe::CraftingSpecialBookCloning
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.recipe.Ingredient import Ingredient
    from generated_symbols.data.util.MinMaxBounds import MinMaxBounds
    from generated_symbols.world.item.ItemStackTemplate import ItemStackTemplate


@dataclass(kw_only=True)
class CraftingSpecialBookCloning:
    source: Ingredient  # The book item.  Its `written_book_contents` component will be copied, with `generation` value increased by 1.  The other components are copied as-is.   The book will be kept in the crafting grid.
    material: Ingredient  # Additional ingredients.  Multiple materials can be used at the same time.  The number of materials beyond the first one will be added to the result count.
    result: ItemStackTemplate
    allowed_generations: MinMaxBounds[Annotated[int, 'Range | `0`-`2` | both inclusive']] | Annotated[int, 'Range | `0`-`2` | both inclusive'] | None = None  # Limits the generation of the `source` item that can be copied. Defaults to allow generation 0 and 1 (original and first copy).


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::recipe::CraftingSpecialBookCloning": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The book item. \\\nIts `written_book_contents` component will be copied, with `generation` value increased by 1. \\\nThe other components are copied as-is. \\\n\\\nThe book will be kept in the crafting grid.",
                "key": "source",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::recipe::Ingredient"
                }
            },
            {
                "kind": "pair",
                "desc": "Additional ingredients. \\\nMultiple materials can be used at the same time. \\\nThe number of materials beyond the first one will be added to the result count.",
                "key": "material",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::recipe::Ingredient"
                }
            },
            {
                "kind": "pair",
                "desc": "Limits the generation of the `source` item that can be copied.\nDefaults to allow generation 0 and 1 (original and first copy).",
                "key": "allowed_generations",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::util::MinMaxBounds"
                    },
                    "typeArgs": [
                        {
                            "kind": "int",
                            "valueRange": {
                                "kind": 0,
                                "min": 0,
                                "max": 2
                            }
                        }
                    ]
                },
                "optional": True
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

