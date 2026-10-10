"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::HeightFoliagePlacer
Local link to file: vanilla_mcdoc/data/worldgen/feature/tree/HeightFoliagePlacer.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class HeightFoliagePlacer(GeneratedModel):
    height: Annotated[int, Field(ge=0, le=16)]
