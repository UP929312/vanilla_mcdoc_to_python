# Generated from symbols.json for ::java::data::worldgen::density_function::Clamp
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.density_function.DensityFunction import DensityFunction
    from generated_symbols.data.worldgen.density_function.NoiseRange import NoiseRange


@dataclass(kw_only=True)
class Clamp:
    input: DensityFunction
    min: NoiseRange
    max: NoiseRange


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::density_function::Clamp": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "input",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::DensityFunction"
                }
            },
            {
                "kind": "pair",
                "key": "min",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::NoiseRange"
                }
            },
            {
                "kind": "pair",
                "key": "max",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::NoiseRange"
                }
            }
        ]
    }
}

