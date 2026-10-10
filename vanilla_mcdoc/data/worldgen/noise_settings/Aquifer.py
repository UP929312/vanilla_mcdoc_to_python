"""
Generated from symbols.json for ::java::data::worldgen::noise_settings::Aquifer
Local link to file: vanilla_mcdoc/data/worldgen/noise_settings/Aquifer.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.density_function.DensityFunctionRef import DensityFunctionRef


class Aquifer(GeneratedModel):
    barrier: DensityFunctionRef
    fluid_level_floodedness: DensityFunctionRef
    fluid_level_spread: DensityFunctionRef
    lava: DensityFunctionRef
    exclusion: DensityFunctionRef
    surface_level: DensityFunctionRef


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::noise_settings::Aquifer": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "barrier",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::DensityFunctionRef"
                }
            },
            {
                "kind": "pair",
                "key": "fluid_level_floodedness",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::DensityFunctionRef"
                }
            },
            {
                "kind": "pair",
                "key": "fluid_level_spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::DensityFunctionRef"
                }
            },
            {
                "kind": "pair",
                "key": "lava",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::DensityFunctionRef"
                }
            },
            {
                "kind": "pair",
                "key": "exclusion",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::DensityFunctionRef"
                }
            },
            {
                "kind": "pair",
                "key": "surface_level",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::DensityFunctionRef"
                }
            }
        ]
    }
}
