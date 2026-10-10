"""
Generated from symbols.json for ::java::assets::item_definition::RangeDispatchEntry
Local link to file: generated_symbols/assets/item_definition/RangeDispatchEntry.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.assets.item_definition.ItemModel import ItemModel


class RangeDispatchEntry(GeneratedModel):
    threshold: float
    model: ItemModel


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::RangeDispatchEntry": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "threshold",
                "type": {
                    "kind": "float"
                }
            },
            {
                "kind": "pair",
                "key": "model",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::item_definition::ItemModel"
                }
            }
        ]
    }
}
