"""
Generated from symbols.json for ::java::data::worldgen::noise_settings::NoiseSlideSettings
Local link to file: vanilla_mcdoc/data/worldgen/noise_settings/NoiseSlideSettings.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class NoiseSlideSettings(GeneratedModel):
    target: float  # The target density. Positive values add terrain and negative values remove terrain.
    size: Annotated[int, Field(ge=0, le=256)]  # Defines a range of 'Size * Size vertical * 4' blocks where the existing density and target are interpolated.
    offset: int  # Defines an range of 'Offset * Size vertical * 4' blocks where the density is set to the target.
