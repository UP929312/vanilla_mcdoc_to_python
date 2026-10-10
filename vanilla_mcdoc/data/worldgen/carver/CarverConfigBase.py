"""
Generated from symbols.json for ::java::data::worldgen::carver::CarverConfigBase
Local link to file: vanilla_mcdoc/data/worldgen/carver/CarverConfigBase.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.HeightProvider import HeightProvider


class CarverConfigBase(GeneratedModel):
    probability: Annotated[float, Field(ge=0, le=1)]
    y: HeightProvider
