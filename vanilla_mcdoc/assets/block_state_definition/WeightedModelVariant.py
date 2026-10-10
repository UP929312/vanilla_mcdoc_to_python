"""
Generated from symbols.json for ::java::assets::block_state_definition::WeightedModelVariant
Local link to file: vanilla_mcdoc/assets/block_state_definition/WeightedModelVariant.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.assets.block_state_definition.ModelVariantBase import ModelVariantBase


class WeightedModelVariant(ModelVariantBase):
    weight: Annotated[int, Field(ge=1)] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::block_state_definition::WeightedModelVariant": {
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
