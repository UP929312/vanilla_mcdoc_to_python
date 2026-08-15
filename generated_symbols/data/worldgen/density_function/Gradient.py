"""
Generated from symbols.json for ::java::data::worldgen::density_function::Gradient
Local link to file: generated_symbols/data/worldgen/density_function/Gradient.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.density_function.NoiseRange import NoiseRange
    from generated_symbols.data.worldgen.density_function.TilingMode import TilingMode
    from generated_symbols.util.direction.Axis import Axis


@dataclass(kw_only=True)
class Gradient:
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

