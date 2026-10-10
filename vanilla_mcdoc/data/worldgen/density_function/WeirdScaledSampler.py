"""
Generated from symbols.json for ::java::data::worldgen::density_function::WeirdScaledSampler
Local link to file: vanilla_mcdoc/data/worldgen/density_function/WeirdScaledSampler.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.density_function.DensityFunctionRef import DensityFunctionRef
    from vanilla_mcdoc.data.worldgen.density_function.NoiseParametersRef import NoiseParametersRef
    from vanilla_mcdoc.data.worldgen.density_function.RarityType import RarityType


class WeirdScaledSampler(GeneratedModel):
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
