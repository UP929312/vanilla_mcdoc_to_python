# Generated from symbols.json for ::java::data::worldgen::density_function::TerrainShaperSpline
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.density_function.DensityFunctionRef import DensityFunctionRef
    from generated_symbols.data.worldgen.density_function.NoiseRange import NoiseRange
    from generated_symbols.data.worldgen.density_function.SplineType import SplineType


@dataclass(kw_only=True)
class TerrainShaperSpline:
    spline: SplineType
    min_value: NoiseRange
    max_value: NoiseRange
    continentalness: DensityFunctionRef
    erosion: DensityFunctionRef
    weirdness: DensityFunctionRef


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::density_function::TerrainShaperSpline": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "spline",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::SplineType"
                }
            },
            {
                "kind": "pair",
                "key": "min_value",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::NoiseRange"
                }
            },
            {
                "kind": "pair",
                "key": "max_value",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::NoiseRange"
                }
            },
            {
                "kind": "pair",
                "key": "continentalness",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::DensityFunctionRef"
                }
            },
            {
                "kind": "pair",
                "key": "erosion",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::DensityFunctionRef"
                }
            },
            {
                "kind": "pair",
                "key": "weirdness",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::DensityFunctionRef"
                }
            }
        ]
    }
}

