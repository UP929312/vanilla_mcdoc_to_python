"""
Generated from symbols.json for ::java::data::worldgen::dimension::biome_source::NoiseParameters
Local link to file: vanilla_mcdoc/data/worldgen/dimension/biome_source/NoiseParameters.py
"""
# ~~~ CODE ~~~
from typing import Annotated, ClassVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class NoiseParameters(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/noise'

    base_octave: Annotated[int, Field(ge=-32, le=32)]
    base_amplitude: Annotated[float, Field(ge=0, le=1000000)] | None = None  # Defaults to 1.0.
    octave_count: Annotated[int, Field(ge=1, le=32)] | None = None  # Defaults to 1.
    normalize: bool | None = None  # Defaults to `true`.
    amplitude_modifiers: Annotated[list[Annotated[float, Field(ge=0, le=1000000)]], Field(max_length=32)] | None = None  # When empty or not present, defaults to all 1.0.  Otherwise, the size must match `octave_count`.
