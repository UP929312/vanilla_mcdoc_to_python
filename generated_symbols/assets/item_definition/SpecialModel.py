# Generated from symbols.json for ::java::assets::item_definition::SpecialModel
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.assets.item_definition.SpecialModelType import SpecialModelType


@dataclass(kw_only=True)
class SpecialModel:
    type: SpecialModelType


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::SpecialModel": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::item_definition::SpecialModelType",
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
                    "registry": "minecraft:special_item_model"
                }
            }
        ]
    }
}

