"""
Generated from symbols.json for ::java::data::recipe::IngredientItem
Local link to file: generated_symbols/data/recipe/IngredientItem.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.registry.KnownItemId import KnownItemId


@dataclass(kw_only=True)
class IngredientItem:
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

