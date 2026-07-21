# Generated from symbols.json for ::java::assets::block_state_definition::WeightedModelVariant
from dataclasses import dataclass
from typing import Annotated
from generated_symbols.assets.block_state_definition.ModelVariantBase import ModelVariantBase


@dataclass(kw_only=True)
class WeightedModelVariant(ModelVariantBase):
    weight: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None


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

