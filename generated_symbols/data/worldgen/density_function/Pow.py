"""
Generated from symbols.json for ::java::data::worldgen::density_function::Pow
Local link to file: generated_symbols/data/worldgen/density_function/Pow.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.density_function.DensityFunctionRef import DensityFunctionRef


class Pow(GeneratedModel):
    base: DensityFunctionRef
    exponent: DensityFunctionRef


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::density_function::Pow": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "base",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::DensityFunctionRef"
                }
            },
            {
                "kind": "pair",
                "key": "exponent",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::DensityFunctionRef"
                }
            }
        ]
    }
}

