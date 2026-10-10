"""
Generated from symbols.json for ::java::data::worldgen::feature::decorator::CountExtraConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/decorator/CountExtraConfig.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class CountExtraConfig(GeneratedModel):
    count: Annotated[int, Field(ge=0)]
    extra_count: Annotated[int, Field(ge=0)]
    extra_chance: Annotated[float, Field(ge=0, le=1)]
