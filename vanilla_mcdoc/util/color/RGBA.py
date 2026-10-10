"""
Generated from symbols.json for ::java::util::color::RGBA
Local link to file: vanilla_mcdoc/util/color/RGBA.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field


type RGBA = int | tuple[Annotated[float, Field(ge=0, le=1)], Annotated[float, Field(ge=0, le=1)], Annotated[float, Field(ge=0, le=1)], Annotated[float, Field(ge=0, le=1)]]
