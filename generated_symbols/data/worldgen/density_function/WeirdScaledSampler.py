"""
Generated from symbols.json for ::java::data::worldgen::density_function::WeirdScaledSampler
Local link to file: generated_symbols/data/worldgen/density_function/WeirdScaledSampler.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.density_function.DensityFunctionRef import DensityFunctionRef
    from generated_symbols.data.worldgen.density_function.NoiseParametersRef import NoiseParametersRef
    from generated_symbols.data.worldgen.density_function.RarityType import RarityType


@dataclass(kw_only=True)
class WeirdScaledSampler:
    rarity_value_mapper: RarityType
    noise: NoiseParametersRef
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
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::NoiseParametersRef"
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

