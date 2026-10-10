"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::CreakingHeartTreeDecorator
Local link to file: vanilla_mcdoc/data/worldgen/feature/tree/CreakingHeartTreeDecorator.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class CreakingHeartTreeDecorator(GeneratedModel):
    probability: Annotated[float, Field(ge=0, le=1)]
