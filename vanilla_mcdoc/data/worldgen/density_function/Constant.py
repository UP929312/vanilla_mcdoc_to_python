"""
Generated from symbols.json for ::java::data::worldgen::density_function::Constant
Local link to file: vanilla_mcdoc/data/worldgen/density_function/Constant.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.density_function.NoiseRange import NoiseRange


class Constant(GeneratedModel):
    value: NoiseRange
