"""
Generated from symbols.json for ::java::data::worldgen::feature::GeodeLayerSettings
Local link to file: vanilla_mcdoc/data/worldgen/feature/GeodeLayerSettings.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class GeodeLayerSettings(GeneratedModel):
    filling: Annotated[float, Field(ge=0.01, le=50)] | None = None
    inner_layer: Annotated[float, Field(ge=0.01, le=50)] | None = None
    middle_layer: Annotated[float, Field(ge=0.01, le=50)] | None = None
    outer_layer: Annotated[float, Field(ge=0.01, le=50)] | None = None
