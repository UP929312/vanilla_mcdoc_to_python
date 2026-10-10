"""
Generated from symbols.json for ::java::data::worldgen::density_function::YClampedGradient
Local link to file: vanilla_mcdoc/data/worldgen/density_function/YClampedGradient.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.density_function.NoiseRange import NoiseRange


class YClampedGradient(GeneratedModel):
    from_y: Annotated[int, Field(ge=-4064, le=4062)]
    to_y: Annotated[int, Field(ge=-4064, le=4062)]
    from_value: NoiseRange
    to_value: NoiseRange
