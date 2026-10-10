"""
Generated from symbols.json for ::java::data::worldgen::feature::decorator::ChanceConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/decorator/ChanceConfig.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class ChanceConfig(GeneratedModel):
    chance: Annotated[int, Field(ge=0)]
