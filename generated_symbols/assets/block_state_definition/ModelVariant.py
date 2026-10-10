"""
Generated from symbols.json for ::java::assets::block_state_definition::ModelVariant
Local link to file: generated_symbols/assets/block_state_definition/ModelVariant.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from generated_symbols.assets.block_state_definition.ModelVariantBase import ModelVariantBase


class ModelVariantStruct(ModelVariantBase):
    weight: Annotated[int, Field(ge=1)] | None = None


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

