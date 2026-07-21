# Generated from symbols.json for ::java::assets::block_state_definition::ModelVariant
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from generated_symbols.assets.block_state_definition.ModelVariantBase import ModelVariantBase


type ModelVariant = ModelVariantBase | list[Any]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::block_state_definition::ModelVariant": {
        "kind": "union",
        "members": [
            {
                "kind": "reference",
                "path": "::java::assets::block_state_definition::ModelVariantBase"
            },
            {
                "kind": "list",
                "item": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "spread",
                            "type": {
                                "kind": "reference",
                                "path": "::java::assets::block_state_definition::ModelVariantBase"
                            }
                        },
                        {
                            "kind": "pair",
                            "key": "weight",
                            "type": {
                                "kind": "int",
                                "valueRange": {
                                    "kind": 0,
                                    "min": 1
                                }
                            },
                            "optional": True
                        }
                    ]
                }
            }
        ]
    }
}

