# Generated from symbols.json for ::java::assets::item_definition::RangeDispatchEntry
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.assets.item_definition.ItemModel import ItemModel


@dataclass(kw_only=True)
class RangeDispatchEntry:
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

