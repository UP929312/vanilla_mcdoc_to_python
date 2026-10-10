"""
Generated from symbols.json for ::java::data::worldgen::density_function::Slice
Local link to file: vanilla_mcdoc/data/worldgen/density_function/Slice.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.density_function.DensityFunctionRef import DensityFunctionRef
    from vanilla_mcdoc.util.direction.Axis import Axis


class Slice(GeneratedModel):
    axis: Axis
    coordinate: int
    input: DensityFunctionRef


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::density_function::Slice": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "axis",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::direction::Axis"
                }
            },
            {
                "kind": "pair",
                "key": "coordinate",
                "type": {
                    "kind": "int"
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
