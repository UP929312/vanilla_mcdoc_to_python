# Generated from symbols.json for ::java::data::worldgen::density_function::WeirdScaledSampler
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.density_function.DensityFunctionRef import DensityFunctionRef
    from generated_symbols.data.worldgen.density_function.RarityType import RarityType


@dataclass(kw_only=True)
class WeirdScaledSampler:
    rarity_value_mapper: RarityType
    noise: str
    input: DensityFunctionRef


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::density_function::WeirdScaledSampler": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "rarity_value_mapper",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::RarityType"
                }
            },
            {
                "kind": "pair",
                "key": "noise",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "worldgen/noise"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "input",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::DensityFunctionRef"
                }
            }
        ]
    }
}

