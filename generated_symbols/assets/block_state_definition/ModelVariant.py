# Generated from symbols.json for ::java::assets::block_state_definition::ModelVariant
from dataclasses import dataclass
from typing import Annotated

from generated_symbols.assets.block_state_definition.ModelVariantBase import ModelVariantBase


@dataclass(kw_only=True)
class ModelVariantStruct(ModelVariantBase):
    weight: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None


type ModelVariant = ModelVariantBase | list[ModelVariantStruct]


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

