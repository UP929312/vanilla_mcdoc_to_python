"""
Generated from symbols.json for ::java::data::worldgen::feature::ProbabilityConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/ProbabilityConfig.py
"""
# ~~~ CODE ~~~
from typing import Annotated, ClassVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class ProbabilityConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    probability: Annotated[float, Field(ge=0, le=1)]
