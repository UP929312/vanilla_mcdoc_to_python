# Generated from symbols.json for ::java::data::worldgen::density_function::Noise
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.density_function.NoiseParametersRef import NoiseParametersRef


@dataclass(kw_only=True)
class Noise:
    noise: NoiseParametersRef
    xz_scale: float
    y_scale: float


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
            }
        ]
    }
}

