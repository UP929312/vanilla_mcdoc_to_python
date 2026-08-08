# Generated from symbols.json for ::java::data::worldgen::density_function::Slice
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.density_function.DensityFunctionRef import DensityFunctionRef
    from generated_symbols.util.direction.Axis import Axis


@dataclass(kw_only=True)
class Slice:
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

