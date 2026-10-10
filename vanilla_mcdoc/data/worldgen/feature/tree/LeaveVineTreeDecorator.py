"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::LeaveVineTreeDecorator
Local link to file: vanilla_mcdoc/data/worldgen/feature/tree/LeaveVineTreeDecorator.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class LeaveVineTreeDecorator(GeneratedModel):
    probability: Annotated[float, Field(ge=0, le=1)]
