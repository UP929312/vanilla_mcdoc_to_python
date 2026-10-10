"""
Generated from symbols.json for ::java::data::worldgen::density_function::Round
Local link to file: vanilla_mcdoc/data/worldgen/density_function/Round.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.density_function.DensityFunctionRef import DensityFunctionRef


class Round(GeneratedModel):
    input: DensityFunctionRef
    multiple: DensityFunctionRef | None = None  # Defaults to constant 1.
