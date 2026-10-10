"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::PaleMossTreeDecorator
Local link to file: vanilla_mcdoc/data/worldgen/feature/tree/PaleMossTreeDecorator.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class PaleMossTreeDecorator(GeneratedModel):
    leaves_probability: Annotated[float, Field(ge=0, le=1)]
    trunk_probability: Annotated[float, Field(ge=0, le=1)]
    ground_probability: Annotated[float, Field(ge=0, le=1)]
