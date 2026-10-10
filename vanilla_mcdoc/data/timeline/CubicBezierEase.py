"""
Generated from symbols.json for ::java::data::timeline::CubicBezierEase
Local link to file: vanilla_mcdoc/data/timeline/CubicBezierEase.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class CubicBezierEase(GeneratedModel):
    cubic_bezier: tuple[Annotated[float, Field(ge=0, le=1)], float, Annotated[float, Field(ge=0, le=1)], float]  # `[x1, y1, x2, y2]` For an easy GUI, check out: https://cubic-bezier.com/
