"""
Generated from symbols.json for ::java::data::worldgen::attribute::modifier::FloatWithAlpha
Local link to file: vanilla_mcdoc/data/worldgen/attribute/modifier/FloatWithAlpha.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class FloatWithAlpha(GeneratedModel):
    value: float
    alpha: Annotated[float, Field(ge=0, le=1)] | None = None  # Defaults to 1.0
