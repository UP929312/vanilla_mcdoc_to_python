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
