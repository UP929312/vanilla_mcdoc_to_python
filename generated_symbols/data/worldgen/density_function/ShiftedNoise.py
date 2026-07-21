# Generated from symbols.json for ::java::data::worldgen::density_function::ShiftedNoise
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.worldgen.density_function.Noise import Noise

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.density_function.DensityFunctionRef import DensityFunctionRef


@dataclass(kw_only=True)
class ShiftedNoise(Noise):
    shift_x: DensityFunctionRef
    shift_y: DensityFunctionRef
    shift_z: DensityFunctionRef


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::density_function::ShiftedNoise": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::Noise"
                }
            },
            {
                "kind": "pair",
                "key": "shift_x",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::DensityFunctionRef"
                }
            },
            {
                "kind": "pair",
                "key": "shift_y",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::DensityFunctionRef"
                }
            },
            {
                "kind": "pair",
                "key": "shift_z",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::DensityFunctionRef"
                }
            }
        ]
    }
}

