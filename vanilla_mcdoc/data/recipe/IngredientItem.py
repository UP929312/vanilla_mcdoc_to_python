"""
Generated from symbols.json for ::java::data::recipe::IngredientItem
Local link to file: vanilla_mcdoc/data/recipe/IngredientItem.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.registry.KnownItemId import KnownItemId


class IngredientItem(GeneratedModel):
    item: Annotated[str, IdSpec(registry='item')] | KnownItemId


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::recipe::IngredientItem": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "item",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "item"
                                }
                            }
                        }
                    ]
                }
            }
        ]
    }
}
