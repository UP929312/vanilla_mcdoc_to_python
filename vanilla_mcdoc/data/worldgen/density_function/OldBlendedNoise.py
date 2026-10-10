"""
Generated from symbols.json for ::java::data::worldgen::density_function::OldBlendedNoise
Local link to file: vanilla_mcdoc/data/worldgen/density_function/OldBlendedNoise.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class OldBlendedNoise(GeneratedModel):
    xz_scale: float
    y_scale: float
    xz_factor: float
    y_factor: float
    smear_scale_multiplier: Annotated[float, Field(ge=1, le=8)]
