"""
Generated from symbols.json for ::java::data::worldgen::density_function::Interpolated
Local link to file: vanilla_mcdoc/data/worldgen/density_function/Interpolated.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.data.worldgen.density_function.OneArgument import OneArgument


class Interpolated(OneArgument):
    cell_size_xz: Annotated[int, Field(ge=1)]
    cell_size_y: Annotated[int, Field(ge=1)]
