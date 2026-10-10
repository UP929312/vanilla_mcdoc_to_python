"""
Generated from symbols.json for ::java::data::worldgen::feature::placement::RandomChanceModifier
Local link to file: vanilla_mcdoc/data/worldgen/feature/placement/RandomChanceModifier.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class RandomChanceModifier(GeneratedModel):
    chance: Annotated[float, Field(ge=0, le=1)]
