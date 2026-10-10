"""
Generated from symbols.json for ::java::data::worldgen::density_function::Noise
Local link to file: vanilla_mcdoc/data/worldgen/density_function/Noise.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.density_function.DensityFunctionRef import DensityFunctionRef
    from vanilla_mcdoc.data.worldgen.density_function.NoiseParametersRef import NoiseParametersRef


class Noise(GeneratedModel):
    noise: NoiseParametersRef
    xz_scale: float
    y_scale: float
    shift_x: DensityFunctionRef | None = None  # Defaults to constant 0.
    shift_y: DensityFunctionRef | None = None  # Defaults to constant 0.
    shift_z: DensityFunctionRef | None = None  # Defaults to constant 0.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::density_function::Noise": {
        "kind": "struct",
        "fields": [
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
                "key": "xz_scale",
                "type": {
                    "kind": "float"
                }
            },
            {
                "kind": "pair",
                "key": "y_scale",
                "type": {
                    "kind": "float"
                }
            },
            {
                "kind": "spread",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "desc": "Defaults to constant 0.",
                            "key": "shift_x",
                            "type": {
                                "kind": "reference",
                                "path": "::java::data::worldgen::density_function::DensityFunctionRef"
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "desc": "Defaults to constant 0.",
                            "key": "shift_y",
                            "type": {
                                "kind": "reference",
                                "path": "::java::data::worldgen::density_function::DensityFunctionRef"
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "desc": "Defaults to constant 0.",
                            "key": "shift_z",
                            "type": {
                                "kind": "reference",
                                "path": "::java::data::worldgen::density_function::DensityFunctionRef"
                            },
                            "optional": True
                        }
                    ]
                }
            }
        ]
    }
}
