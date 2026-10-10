"""
Generated from symbols.json for ::java::data::worldgen::density_function::Gradient
Local link to file: vanilla_mcdoc/data/worldgen/density_function/Gradient.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.density_function.NoiseRange import NoiseRange
    from vanilla_mcdoc.data.worldgen.density_function.TilingMode import TilingMode
    from vanilla_mcdoc.util.direction.Axis import Axis


class Gradient(GeneratedModel):
    axis: Axis
    tiling: TilingMode | None = None  # Defaults to `clamp_to_edge`.
    from_coordinate: int
    to_coordinate: int
    from_value: NoiseRange
    to_value: NoiseRange


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::density_function::Gradient": {
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
                "desc": "Defaults to `clamp_to_edge`.",
                "key": "tiling",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::TilingMode"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "from_coordinate",
                "type": {
                    "kind": "int"
                }
            },
            {
                "kind": "pair",
                "key": "to_coordinate",
                "type": {
                    "kind": "int"
                }
            },
            {
                "kind": "pair",
                "key": "from_value",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::NoiseRange"
                }
            },
            {
                "kind": "pair",
                "key": "to_value",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::NoiseRange"
                }
            }
        ]
    }
}
