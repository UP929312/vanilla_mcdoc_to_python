# Generated from symbols.json for ::java::data::worldgen::noise_settings::TerrainShaper
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.density_function.CubicSpline import CubicSpline


@dataclass(kw_only=True)
class TerrainShaper:
    offset: CubicSpline
    factor: CubicSpline
    jaggedness: CubicSpline


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::noise_settings::TerrainShaper": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "offset",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::CubicSpline"
                }
            },
            {
                "kind": "pair",
                "key": "factor",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::CubicSpline"
                }
            },
            {
                "kind": "pair",
                "key": "jaggedness",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::CubicSpline"
                }
            }
        ]
    }
}

