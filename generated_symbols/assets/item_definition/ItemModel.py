# Generated from symbols.json for ::java::assets::item_definition::ItemModel
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.assets.item_definition.ItemModeltype import ItemModeltype


@dataclass(kw_only=True)
class ItemModel:
    type: ItemModeltype


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::ItemModel": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::item_definition::ItemModeltype",
                    "attributes": [
                        {
                            "name": "id"
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "type"
                            ]
                        }
                    ],
                    "registry": "minecraft:item_model"
                }
            }
        ]
    }
}

