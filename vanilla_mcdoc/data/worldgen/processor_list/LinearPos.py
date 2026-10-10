"""
Generated from symbols.json for ::java::data::worldgen::processor_list::LinearPos
Local link to file: vanilla_mcdoc/data/worldgen/processor_list/LinearPos.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class LinearPos(GeneratedModel):
    min_dist: Annotated[int, Field(ge=0, le=255)] | None = None
    max_dist: Annotated[int, Field(ge=0, le=255)] | None = None
    min_chance: Annotated[float, Field(ge=0, le=1)] | None = None
    max_chance: Annotated[float, Field(ge=0, le=1)] | None = None
