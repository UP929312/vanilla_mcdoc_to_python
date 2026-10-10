"""
Generated from symbols.json for ::java::data::worldgen::noise_settings::TerrainShaper
Local link to file: vanilla_mcdoc/data/worldgen/noise_settings/TerrainShaper.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.density_function.CubicSpline import CubicSpline


class TerrainShaper(GeneratedModel):
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
