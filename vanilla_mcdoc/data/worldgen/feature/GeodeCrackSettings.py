"""
Generated from symbols.json for ::java::data::worldgen::feature::GeodeCrackSettings
Local link to file: vanilla_mcdoc/data/worldgen/feature/GeodeCrackSettings.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class GeodeCrackSettings(GeneratedModel):
    generate_crack_chance: Annotated[float, Field(ge=0, le=1)] | None = None
    base_crack_size: Annotated[float, Field(ge=0, le=5)] | None = None
    crack_point_offset: Annotated[int, Field(ge=0, le=10)] | None = None
