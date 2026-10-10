"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::ThreeLayersFeatureSize
Local link to file: vanilla_mcdoc/data/worldgen/feature/tree/ThreeLayersFeatureSize.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class ThreeLayersFeatureSize(GeneratedModel):
    min_clipped_height: Annotated[float, Field(ge=0, le=80)] | None = None
    limit: Annotated[int, Field(ge=0, le=80)] | None = None
    upper_limit: Annotated[int, Field(ge=0, le=80)] | None = None
    lower_size: Annotated[int, Field(ge=0, le=16)] | None = None
    middle_size: Annotated[int, Field(ge=0, le=16)] | None = None
    upper_size: Annotated[int, Field(ge=0, le=16)] | None = None
