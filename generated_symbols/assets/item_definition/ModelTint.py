# Generated from symbols.json for ::java::assets::item_definition::ModelTint
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.assets.item_definition.TintSourceType import TintSourceType


@dataclass(kw_only=True)
class ModelTint:
    type: TintSourceType


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::ModelTint": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::item_definition::TintSourceType",
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
                    "registry": "minecraft:tint_source"
                }
            }
        ]
    }
}

