"""
Generated from symbols.json for ::java::data::worldgen::feature::TwistingVinesConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/TwistingVinesConfig.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class TwistingVinesConfig(GeneratedModel):
    spread_width: Annotated[int, Field(ge=1)]
    spread_height: Annotated[int, Field(ge=1)]
    max_height: Annotated[int, Field(ge=1)]
