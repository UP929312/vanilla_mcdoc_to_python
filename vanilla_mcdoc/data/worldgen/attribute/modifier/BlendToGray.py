"""
Generated from symbols.json for ::java::data::worldgen::attribute::modifier::BlendToGray
Local link to file: vanilla_mcdoc/data/worldgen/attribute/modifier/BlendToGray.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class BlendToGray(GeneratedModel):
    brightness: Annotated[float, Field(ge=0, le=1)]  # The gray color is `brightness * (0.3 * r + 0.59 * g + 0.11 * b)`.
    factor: Annotated[float, Field(ge=0, le=1)]  # The factor to mix with.
