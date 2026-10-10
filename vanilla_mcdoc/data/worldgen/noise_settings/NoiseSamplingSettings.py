"""
Generated from symbols.json for ::java::data::worldgen::noise_settings::NoiseSamplingSettings
Local link to file: vanilla_mcdoc/data/worldgen/noise_settings/NoiseSamplingSettings.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class NoiseSamplingSettings(GeneratedModel):
    xz_scale: Annotated[float, Field(ge=0.001, le=1000)]
    y_scale: Annotated[float, Field(ge=0.001, le=1000)]
    xz_factor: Annotated[float, Field(ge=0.001, le=1000)]
    y_factor: Annotated[float, Field(ge=0.001, le=1000)]
