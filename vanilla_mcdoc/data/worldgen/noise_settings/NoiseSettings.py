"""
Generated from symbols.json for ::java::data::worldgen::noise_settings::NoiseSettings
Local link to file: vanilla_mcdoc/data/worldgen/noise_settings/NoiseSettings.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class NoiseSettings(GeneratedModel):
    min_y: Annotated[int, Field(ge=-2048, le=2047)]  # Minimum height where blocks start generating.
    height: Annotated[int, Field(ge=0, le=4096)]  # The total height where blocks can generate. Max Y = Min Y + Height.
